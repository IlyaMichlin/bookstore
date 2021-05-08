from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignupPageView


# Create your tests here.
class CustomUserTest(TestCase):
    test_username = 'test_user'
    test_email = 'test_user@mail.com'
    test_password = 'testpass123'
    test_super_username = 'test_super_user'
    test_super_email = 'test_super_user@mail.com'
    test_super_password = 'testsuperpass123'

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username=self.test_username,
            email=self.test_email,
            password=self.test_password,
        )
        self.assertEqual(user.username, self.test_username)
        self.assertEqual(user.email, self.test_email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username=self.test_super_username,
            email=self.test_super_email,
            password=self.test_super_password,
        )
        self.assertEqual(user.username, self.test_super_username)
        self.assertEqual(user.email, self.test_super_email)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Text not in template.')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
