#!/usr/bin/python3

"""
    Module: test_file_storage.py
    This module contains the tests for the file_storage class
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
        TestFileStorage: holds all the test cases for the FileStorage.py module
    """

    def test_file_path_is_private(self):
        """
            tests that the file path is a private variable
        """
        storage = FileStorage()
        with self.assertRaises(AttributeError):
            storage.__file_path
            FileStorage.__file_path

    def test_file_path_is_class_attribute(self):
        """
            tests that __file_path is a private class attr
        """
        storage = FileStorage()
        msg = "Expects __file_path to be a class attribute"
        msg2 = "Expects __file_path to be a class attribute but got instance\
        attribute"

        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'), msg)
        self.assertNotIn('_FileStorage__file_path', storage.__dict__.keys(),
                         msg2)

    def test_file_path_is_string(self):
        """
            test that the __file_path is of type string
        """

        msg = "Expected __file_path to type 'str' but got {}".format(
            type(FileStorage._FileStorage__file_path))

        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

    def test_objects_is_private(self):
        """
            tests that __object is private class variable
        """
        storage = FileStorage()
        with self.assertRaises(AttributeError):
            storage.__objects
            FileStorage.__objects

    def test_objects_is_class_attribute(self):
        """
            tests that __objects is private class attr
        """
        storage = FileStorage()
        msg = "Expects __objects to be a class attribute"
        msg2 = "Expected __objects to be a class attribute but got instance\
                attribute"
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'), msg)
        self.assertNotIn('__objects', storage.__dict__.keys(), msg)

    def test_objects_is_dict(self):
        """
            tests that __objects is of type dict
        """
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_objects_stores_data_in_correct_format(self):
        """
            tests that data stored in __objects is stored in the correct format
            Example:
                BaseModel with id 1213
                the key shall be BaseModel.1213
            the values should json strings
        """
        model = BaseModel()
        storage = FileStorage()
        storage.new(model)
        key = '{}.{}'.format(type(model).__name__, model.id)

        self.assertIn(key, FileStorage._FileStorage__objects)
        self.assertIs(model,
                      FileStorage._FileStorage__objects[key])

    def test_all_function_is_present(self):
        """
            tests that all() is present
        """
        msg = "Expected FileStorage to have function 'all'"

        self.assertTrue(hasattr(FileStorage, 'all'), msg)

    def test_all_returns_dict(self):
        """
            tests that all() returns a dict
        """
        storage = FileStorage()
        actual = storage.all()
        self.assertIsInstance(actual, dict)

    def test_all_returns_object(self):
        """
            tests that all() returns __object
        """
        storage = FileStorage()
        actual = storage.all()
        self.assertIs(FileStorage._FileStorage__objects, actual)

    def test_new_function(self):
        """
            tests that new() is present
        """
        msg = "Expected FileStorage to have function 'new'"
        self.assertTrue(hasattr(FileStorage, 'new'), msg)

    def test_new_sets_object_in_objects(self):
        """
            tests that new() sets given objects into __objects
        """
        model = BaseModel()
        storage = FileStorage()
        storage.new(model)
        key = '{}.{}'.format(type(model).__name__, model.id)
        self.assertIn(key, FileStorage._FileStorage__objects)
        self.assertIs(model,
                      FileStorage._FileStorage__objects[key])

    def test_save_is_present(self):
        """
            tests that the save() is present
        """
        msg = "Expected FileStorage to have fnction 'save'"
        self.assertTrue(hasattr(FileStorage, 'save'), msg)

    def test_save_serializes_objects_to_file(self):
        """
            tests that the save function serializes objects.
            serializes __objects to a file
        """
        pass
