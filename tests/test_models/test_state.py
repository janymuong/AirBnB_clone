#!/usr/bin/python3
"""
    test_state:
        module has tests for the state model
"""


import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
        class for all unit tests for the state model
    """

    def test_state_inherits_from_base_model(self):
        """
            tests that the state model inherits from BaseModel
        """
        msg = "Expected State to inherit from BaseModel"

        self.assertTrue(issubclass(State, BaseModel), msg)

    def test_state_has_attribute_name(self):
        """
            test that State has public class attr name
        """

        msg = "Expected State to have public class attribute 'name'"
        self.assertTrue(hasattr(State, 'name'), msg)

    def test_attribute_name_is_empty_string(self):
        """
            test that class attribute name is an empty string
        """
        msg = "Expected name to be an empty string"
        length = 0
        self.assertEqual(len(State.name), length, msg)
        self.assertEqual(State.name, "")

    def test_instance_has_default_name_value(self):
        """
            test that instances of State get default name value
        """
        msg = "Expected object to have default name value"

        state = State()
        self.assertEqual(len(state.name), 0)
        self.assertEqual(state.name, "")

    def test_instance_sets_own_name(self):
        """
            test that instance can set it own value
        """
        state = State()
        name = "Kenya"
        state.name = name

        self.assertEqual(name, state.name)
        self.assertNotEqual(state.name, State.name)
