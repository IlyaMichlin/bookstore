from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve


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
    test_username = 'testuser'
    test_email = 'testuser@mail.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Text not in template.')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.test_username,
            self.test_email,
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.test_username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.test_email)
