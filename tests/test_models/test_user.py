#!/usr/bin/python3
"""
    test_user:
        This module contains unit tests for the User model
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
        TestUser:
            testing class for User model
    """

    def test_user_inherits_base_model(self):
        """
            test that user is a subclass of BaseModel
        """
        msg = "Expected User to be a subclass of the BaseModel class"

        self.assertTrue(issubclass(User, BaseModel), msg)

    def test_class_attribute_email(self):
        """
            test that User class has a public class attr email
        """
        msg = "Expected User class to have public class attribute 'Email'"
        self.assertTrue(hasattr(User, 'email'), msg)

    def test_email_is_empty_string(self):
        """
            test the email is empty string
        """
        msg = "Expected email to be empty string"
        length = 0
        self.assertEqual(len(User.email), length, msg)
        self.assertEqual(User.email, "")

    def test_email_is_public_class_attr(self):
        """
            test that email is a public class attr
        """
        user = User()
        msg = "Expected email to not be an instance attribute"
        self.assertNotIn('email', user.__dict__.keys(), msg)

    def test_instance_cannot_set_class_attribute_email(self):
        """
            test that an instance cannot change the class attr email
        """

        user = User()
        user.email = "email"
        self.assertEqual(User.email, "")
        self.assertNotEqual(User.email, user.email)

    def test_user_instance_has_default_class_email(self):
        """
            test that user instance has the default email
        """

        user = User()
        self.assertEqual(user.email, User.email)
        self.assertEqual(user.email, "")

    def test_class_attribute_password(self):
        """
            test that User class has a public class attr password
        """
        msg = "Expected User class to have public class attribute 'password'"
        self.assertTrue(hasattr(User, 'password'), msg)

    def test_password_is_empty_string(self):
        """
            test the password is empty string
        """
        msg = "Expected password to be empty string"
        length = 0
        self.assertEqual(len(User.password), length, msg)
        self.assertEqual(User.password, "")

    def test_password_is_public_class_attr(self):
        """
            test that pasword is a public class attr
        """
        user = User()
        msg = "Expected password to not be an instance attribute"
        self.assertNotIn('password', user.__dict__.keys(), msg)

    def test_instance_cannot_set_class_attribute_password(self):
        """
            test that an instance cannot change the class attr password
        """

        user = User()
        user.password = "pwd"
        self.assertEqual(User.password, "")
        self.assertNotEqual(User.password, user.password)

    def test_user_instance_has_default_class_password(self):
        """
            test that user instance has the default password
        """

        user = User()
        self.assertEqual(user.password, User.password)
        self.assertEqual(user.password, "")

    def test_class_attribute_first_name(self):
        """
            test that User class has a public class attr first_name
        """
        msg = "Expected User class to have public class attribute 'first_name'"
        self.assertTrue(hasattr(User, 'first_name'), msg)

    def test_first_name_is_empty_string(self):
        """
            test the first_name is empty string
        """
        msg = "Expected first_name to be empty string"
        length = 0
        self.assertEqual(len(User.first_name), length, msg)
        self.assertEqual(User.first_name, "")

    def test_first_name_is_public_class_attr(self):
        """
            test that first_name is a public class attr
        """
        user = User()
        msg = "Expected first_name to not be an instance attribute"
        self.assertNotIn('first_name', user.__dict__.keys(), msg)

    def test_instance_cannot_set_class_attribute_first_name(self):
        """
            test that an instance cannot change the class attr first_name
        """

        user = User()
        user.first_name = "name"
        self.assertEqual(User.first_name, "")
        self.assertNotEqual(User.first_name, user.first_name)

    def test_user_instance_has_default_class_first_name(self):
        """
            test that user instance has the default first_name
        """

        user = User()
        self.assertEqual(user.first_name, User.first_name)
        self.assertEqual(user.first_name, "")

    def test_class_attribute_last_name(self):
        """
            test that User class has a public class attr last_name
        """
        msg = "Expected User class to have public class attribute 'last_name'"
        self.assertTrue(hasattr(User, 'last_name'), msg)

    def test_last_name_is_empty_string(self):
        """
            test the last_name is empty string
        """
        msg = "Expected last_name to be empty string"
        length = 0
        self.assertEqual(len(User.last_name), length, msg)
        self.assertEqual(User.last_name, "")

    def test_last_name_is_public_class_attr(self):
        """
            test that last_name is a public class attr
        """
        user = User()
        msg = "Expected last_name to not be an instance attribute"
        self.assertNotIn('last_name', user.__dict__.keys(), msg)

    def test_instance_cannot_set_class_attribute_last_name(self):
        """
            test that an instance cannot change the class attr last_name
        """

        user = User()
        user.last_name = "L.name"
        self.assertEqual(User.last_name, "")
        self.assertNotEqual(User.last_name, user.last_name)

    def test_user_instance_has_default_class_last_name(self):
        """
            test that user instance has the default last_name
        """

        user = User()
        self.assertEqual(user.last_name, User.last_name)
        self.assertEqual(user.last_name, "")
