#!/usr/bin/python3
"""
    Test module for the Base model class
    Base model class defines common attributes/methods for other classes\
            that inherit from it
"""
import unittest
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
        unit tests for the BaseModel class
    """

    def test_id_is_present(self):
        """
            test that that public instance attribute id is present
        """
        model = BaseModel()
        msg = "Expected {} to have public instance attribute id".format(
            type(model).__name__)
        self.assertTrue(hasAttr(model, 'id'), msg)
        self.assertIn('id', model.__dict__.keys(), msg)

    def test_id_is_unique(self):
        """
            test that each instance has a unique id
        """
        model1 = BaseModel()
        model2 = BaseModel()
        id1 = model1.id
        id2 = model2.id
        msg = "Expected {} to not be equal to {}".format(id1, id2)
        self.assertNotEqual(id1, id2)

    def test_id_is_string(self):
        """
            test that id is a string
        """
        model = BaseModel()
        msg = "Expected attribute id to be str but got {}".format(
            type(model.id).__name__)
        self.assertIsInstance(model.id, str, msg)
        self.assertTrue(type(model.id) == str, msg)

    def test_id_is_not_other_data_types(self):
        """
            test that id is not other data types
        """
        model = BaseModel()
        msg = "Expected attribute id to be str but got {}".format(
            type(model.id).__name__)
        self.assertIsNotInstance(
            model.id, (int, float, bool, dict, set, tuple, list), msg)

    def test_id_length(self):
        """
            test that id has correct length
        """
        model = BaseModel()
        expected = 32
        actual = len(model.id)
        msg = "Expected id length to be {} but got {}\nExpected:\n\t{}\n\
                Actual:\n\t{}"
        self.assertEqual(expected, actual, msg)
        self.assertFalse(expected > actual, msg)

    def test_id_is_not_empty_string(self):
        """
            test that id is not blank spaces/empty string
            test that id is not made of whitespace " \t\n"
        """
        model = BaseModel()
        msg = "Expected id to be non-blank"
        assert not model.id.isspace(), msg

    def test_id_is_uuid(self):
        """
            test that id is a valid uuid
            Raises a valueError if id is not a valid UUID
        """
        model = BaseModel()
        msg = "Expected id to be uuid format-{}(uuidv4) but got '{}'".format(
                uuid.uuidv4(), model.id)
        assert uuid.UUID(model.id), msg
