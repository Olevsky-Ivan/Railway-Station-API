from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


class CustomUserModelTest(TestCase):
    def setUp(self):
        self.email = "testuser@example.com"
        self.password = "password123"
        self.User = get_user_model()

    def test_create_user(self):
        user = self.User.objects.create_user(email=self.email, password=self.password)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        superuser = self.User.objects.create_superuser(email=self.email, password=self.password)
        self.assertEqual(superuser.email, self.email)
        self.assertTrue(superuser.check_password(self.password))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError):
            self.User.objects.create_user(email="", password=self.password)

    def test_create_superuser_without_is_staff(self):
        with self.assertRaises(ValueError):
            self.User.objects.create_superuser(email=self.email, password=self.password, is_staff=False)

    def test_create_superuser_without_is_superuser(self):
        with self.assertRaises(ValueError):
            self.User.objects.create_superuser(email=self.email, password=self.password, is_superuser=False)
