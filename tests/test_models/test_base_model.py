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

    def test_createdAt_updatedAt_is_present(self):
        """
            test that that public instance attribute created_at\
                    & updated_at is present
        """
        model = BaseModel()
        msg = "Expected {} to have public instance attributes\
                created_at and updated_at".format(
            type(model).__name__)
        self.assertTrue(hasAttr(model, 'created_at'), msg)
        self.assertTrue(hasAttr(model, 'updated_at'), msg)

        self.assertIn('created_at', model.__dict__.keys(), msg)
        self.assertIn('updated_at', model.__dict__.keys(), msg)

    def test_createdAt_updatedAt_is_set_to_current_time_on_create(self):
        """
            tests that created_at and updated_at are set to the current time\
                    when object is created
        """
        model = BaseModel()

        self.assertAlmostEqual(model.created_at, datetime.now(),
                               delta=timedelta(milliseconds=10),
                               "Expected created_at to be set to time now on\
                                       creation.")
        self.assertAlmostEqual(model.updated_at, datetime.now(),
                               delta=timedelta(milliseconds=10),
                               "Expected updated_at to be set to time now on\
                                       creattion.")

    def test_created_at_and_updated_at_are_equal_on_create(self):
        """
            tests that created_at == updated_at on create
        """
        model = BaseModel()

        msg = "Expected created_at: {} to be equal to updated_at: {}".format(
            model.created_at, model.updated_at)

        self.assertEqual(model.created_at, model.updated_at, msg)

    def test_updated_at_is_updated_on_updates(self):
        """
            tests that updated_at is updated when object is changed
        """
        model = BaseModel()

        updated_at = model.updated_at

        model.update = "this is an update"

        msg = "Expected updated_at:[before update] {} not to be equal to\
                updated_at: [after update] {}".format(
            updated_at, model.updated_at)
        self.assertNotEqual(updated_at, model.updated_at, msg)

    def test_updated_at_is_set_to_current_time_on_update(self):
        """
            test that updated_at is set to current time on updated
        """
        model = BaseModel()
        model.update = "this is an update"
        msg = "Expected updated_at to be set to current time on update\n.\
                Expected:\n\t{}\nActual:\n\t{}".format(datetime.now(),
                                                       model.updated_at)

        self.assertAlmostEqual(model.updated_at, datetime.now(),
                               delta=timedelta(milliseconds=10), msg)

    def test_created_at_not_updated_on_updates(self):
        """
            test that created_at is not updated when an update is done
        """
        model = BaseModel()

        created_at = model.created_at

        model.update = "this is an update"

        msg = "Expected created_at to not be updated on updates.\nExpected:\
                \n\t{}\nActual:\n\t{}".format(created_at, model.created_at)

        self.assertEqual(created_at, model.created_at, msg)

    def test_updated_at_greater_than_created_at_on_updates(self):
        """
            test that updated_at is greater than created_at after update
        """
        model = BaseModel()
        created_at = model.created_at

        model.update = "is an update"

        msg = "Expected updated_at: {} to be > than created_at: {} after\
                update".format(model.updated_at, model.created_at)

        self.assertGreater(model.updated_at, created_at, msg)

    def test_updated_at_and_created_at_is_datetime(self):
        """
            test that updated_at and created_at are datetime objects
        """
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_method_is_present(self):
        """
            tests that the __str__ function is available
        """
        model = BaseModel()
        msg = "Expected {} to have a __str__ function".format(
            type(model).__name__)
        self.assertTrue(hasAttr(model, '__str__'), msg)
        self.assertIn('__str__', model.__dict__.keys(), msg)

    def test_str_method_returns_string(self):
        """
            test that return value of __str__ is a string
        """
        model = BaseModel()
        value = str(model)
        msg = "Expected return value of __str__ to string but got {}".format(
            type(value))
        self.assertIsInstance(value, str, msg)
        self.assertTrue(type(value) == str, msg)

    def test_str_return_is_correct_format(self):
        """
            tests that the return value of __str__ is in stipulated format
        """
        model = BaseModel()
        expected = "[{}] ({}) {}".format(
            type(model).__name__, model.id, model.__dict__)
        actual = str(model)
        msg = "Expected {} but got {}\nExpected:\n\t{}\nActual:\n\t{}".format(
            expected, actual, expected, actual)
        self.assertEqual(expected, actual, msg)

    def test_save_function_is_present(self):
        """
            tests that BaseModel has function save()
        """
        model = BaseModel()
        msg = "Expected {} to have a 'save()' function".format(
            type(model).__name__)

        self.assertTrue(hasAttr(model, 'save'), msg)
        self.assertIn('save', model.__dict__.keys(), msg)

    def test_save_function_updates_updated_at_with_current_time(self):
        """
            tests that the on calling save(), the public attribute created_at\
                    is updated with the current time
        """
        model = BaseModel()
        model.save()
        expected = datetime.now()
        actual = model.updated_at
        msg = "Expected updated_at to be updated with the current time {} but\
                but got {}".format(expected, actual)

        self.assertAlmostEqual(expected, actual,
                               delta=timedelta(10=milliseconds), msg)

    def test_to_dict_is_present(self):
        """
            tests that the to_dict function is defined
        """
        model = BaseModel()
        msg = "Expected {} to have a 'to_dict' function".format(
            type(model).__name__)

        self.assertTrue(hasAttr(model, 'to_dict'), msg)

    def test_to_dict_return_value_is_dictionary(self):
        """
            tests the return value of to_dict is a dictionary
        """
        model = BaseModel()
        actual = model.to_dict()
        msg = "Expected return value to be a dictionary but got {}".format(
            type(actual))

        self.assertIsInstance(actual, dict)

    def test_to_dict_return_value_not_empty(self):
        """
            tests that the return value of to_dict is not an empty dict
        """
        model = BaseModel()
        actual = model.to_dict()
        msg = "Expected return value to not be an empty dict but got\
                {}".format(actual)
        self.assertTrue(bool(actual), msg)

    def test_to_dict_return_value_has_attr_class(self):
        """
            tests that the return value(dict) has key __class__
            tests that value of __class__ is name of object's class
        """
        model = BaseModel()
        actual = model.to_dict()
        msg = "Expected the returned dict to have key '__class__'"

        self.assertIn("__class__", actual, msg)
        self.assertEqual(actual.__class__, type(model).__name__, "Expected\
                value of __class__ to be 'BaseModel' but got {}".format(
            actual.__class__))

    def test_to_dict_return_value_has_values_of_dict(self):
        """
            tests that returned dict from to_dict has all the key/value\
                    pairs of __dict__
        """
        model = BaseModel()
        actual = model.to_dict()
        msg = "Expected all key/values here: {} to be in {}".format(
            model.__dict__, actual)

        self.assertDictContainSubset(model.__dict__, actual, msg)

    def test_created_at_and_updated_saved_as_str(self):
        """
            test that created_at and updated_at are str objects when\
                    serialized into dict
        """
        model = BaseModel()
        dict_value = model.to_dict()
        self.assertIsInstance(dict_value.created_at, str)
        self.assertTrue(type(dict_value.created_at) == str)
        self.assertIsInstance(dict_value.updated_at, str)
        self.assertTrue(type(dict_value.updated_at) == str)

    def test_created_at_and_updated_at_are_from_datetime(self):
        """
            test that created_at and updated_at were created from datetime\
                    objects and serialized in correct format
        """
        model = BaseModel()
        dict_value = model.to_dict()
        isoFormat = "%Y-%m-%dT%H:%M:%S.%f"
        created_datetime = datetime.strptime(dict_value.created_at, isoFormat)
        updated_datetime = datetime.strptime(dict_value.updated_at, isoFormat)

        self.assertIsInstance(created_datetime, datetime)
        self.assertIsInstance(updated_datetime, datetime)