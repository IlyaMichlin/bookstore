from django.contrib.auth import get_user_model
from django.test import TestCase


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
