#!/usr/bin/python3
"""
    test_amenity:
        this module holds the tests for the Amenity model
"""

import unittest

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
        tests for the Amenity model
    """

    def test_amenity_inherits_from_base_model(self):
        """
            test that Amenity inherity from BaseModel
        """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_has_attribute_name(self):
        """
            test that Amenity has public class attr name
        """

        msg = "Expected Amenity to have public class attribute 'name'"
        self.assertTrue(hasattr(Amenity, 'name'), msg)

    def test_attribute_name_is_empty_string(self):
        """
            test that class attribute name is an empty string
        """
        msg = "Expected name to be an empty string"
        length = 0
        self.assertEqual(len(Amenity.name), length, msg)
        self.assertEqual(Amenity.name, "")

    def test_instance_has_default_name_value(self):
        """
            test that instances of Amenity get default name value
        """
        msg = "Expected object to have default name value"

        amenity = Amenity()
        self.assertEqual(len(amenity.name), 0)
        self.assertEqual(amenity.name, "")

    def test_instance_sets_own_name(self):
        """
            test that instance can set it own value
        """
        amenity = Amenity()
        name = "Gym"
        amenity.name = name

        self.assertEqual(name, amenity.name)
        self.assertNotEqual(amenity.name, Amenity.name)

    def test_name_attribute_is_class_attribute(self):
        """
            test that name is a class attribute
        """
        amenity = Amenity()
        msg = "Expected name to be class attribute but got instance attribute"

        self.assertNotIn('name', amenity.__dict__.keys(), msg)
