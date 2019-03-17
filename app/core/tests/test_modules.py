from django.test import TestCase
from django.contrib.auth import get_user_model


class ModuleTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""

        # Arrange
        sample_user = {'email': 'test@psykesolutions.com',
                       'password': 'Testpass123'}
        # Act
        user = get_user_model().objects.create_user(**sample_user)
        # Assert
        self.assertEqual(user.email, sample_user['email'])
        self.assertTrue(user.check_password(sample_user['password']))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        # Arrange
        sample_user = {'email': 'test@PSYKESOLUTIONS.COM',
                       'password': 'Testpass123'}
        # Act
        user = get_user_model().objects.create_user(**sample_user)
        # Assert
        self.assertEqual(user.email, sample_user['email'].lower())

    def test_new_user_email_is_mandatory(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@psykesolutions.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
