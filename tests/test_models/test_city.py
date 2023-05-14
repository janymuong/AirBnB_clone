#!/usr/bin/python3
"""
    test_city:
        this module contains test for the City model
"""

import unittest
from models.city import City
from models.base_model import BaseModel
from models.state import State


class TestCity(unittest.TestCase):
    """
        Test Class for the City test cases
    """

    def test_city_inherits_from_base_model(self):
        """
            tests that city inherits from base model
        """
        msg = "Expected City to inherit from BaseModel"
        self.assertTrue(issubclass(City, BaseModel), msg)

    def test_city_has_class_attribute_state(self):
        """
            test that city has public class attribute state_id
        """
        msg = "Expected City to have public class attribute state_id"
        self.assertTrue(hasattr(City, 'state_id'), msg)

    def test_state_id_is_empty_string(self):
        """
            test that default value of state_id is empty string
        """
        length = 0

        self.assertEqual(len(City.state_id), length)
        self.assertEqual(City.state_id, "")

    def test_state_id_is_set_correct(self):
        """
            test that state_id is equivalent to state.id
        """

        city = City()
        state = State()
        id_num = state.id
        city.state_id = id_num

        self.assertTrue(city.state_id == state.id)

    def test_state_id_set_incorrectly(self):
        """
            test incorrect state_id
        """
        city = City()
        state = State()

        city.state_id = "123456"

        self.assertNotEqual(city.state_id, state.id)

    def test_state_id_is_string(self):
        """
            test that state_id is of type string
        """
        city = City()
        state = State()
        city.state_id = state.id

        self.assertIsInstance(city.state_id, str)

    def test_state_id_not_empty_on_set(self):
        """
            test the instance state_id is not empty string
        """
        city = City()
        state = State()

        city.state_id = state.id

        self.assertNotEqual(city.state_id, "")
        self.assertNotEqual(len(city.state_id), 0)
        self.assertFalse(city.state_id.isspace())

    def test_attribute_name_is_present(self):
        """
            test that City has public class attribute name
        """
        msg = "Expected City to have public class attribute 'name'"

        self.assertTrue(hasattr(City, 'name'), msg)

    def test_attribute_name_is_empty_string(self):
        """
            test that name is empty string by default
        """
        length = 0

        self.assertEqual(len(City.name), length)
        self.assertEqual(City.name, "")

    def test_name_attribute_is_class_attribute(self):
        """
            test that name is a public class attribute
        """
        city = City()
        msg = "Expected name to be class attribute but got instance"
        self.assertNotIn('name', city.__dict__.keys(), msg)

    def test_city_instances_get_default_name(self):
        """
            test that instances of City get default name
        """
        city = City()

        self.assertTrue(City.name == city.name)
        self.assertTrue(city.name == "")
