from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@psykesolutions.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


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

    def test_tag_str(self):
        """Test the Tag string representaion"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the Ingredient string representaion"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Test the Recipe string representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Steak and mushroom sauce',
            time_minutes=5,
            price=5.00,
        )

        self.assertEqual(str(recipe), recipe.title)

    @patch('uuid.uuid4')
    def test_recipe_file_name_uuid(self, mock_uuid):
        """Test that image is saved in the correct location"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid

        file_path = models.recipe_image_file_path(None, 'myimage.jpg')

        exp_path = f'uploads/recipe/{uuid}.jpg'
        self.assertEqual(file_path, exp_path)

    @patch('uuid.uuid4')
    def test_recipe_file_path_with_invalid_name(self, mock_uuid):
        """Test that invalid file name raises exception"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid

        payload = {'instance': None, 'filename': 'myimage'}
        self.assertRaises(ValueError, models.recipe_image_file_path, **payload)
