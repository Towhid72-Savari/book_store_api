from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test the models work properly"""

    def test_create_user_with_email(self):
        """Test creating a new user with an email is successful"""
        email = 'test@test.com'
        password = 'Testpass'
        user = get_user_model().objects.create_user(
            email=email, password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(
            email, 'Test123'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_email_invalid(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpass')

    def test_create_new_superuser(self):
        """Test creating a new superuser is successful"""
        email = 'suoeruser@test.com'
        password = 'supertest'
        superuser = get_user_model().objects.create_superuser(
            email=email, password=password
        )
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
