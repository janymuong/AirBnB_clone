#!/usr/bin/python3
'''module: test_review:
unittests for Review class: test cases/edge cases
'''

import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    '''this class represents the Review class test case'''

    def setUp(self):
        '''setUp
        define test variables and initializers
        '''

        self.mock_data = {
            "id": "test_id",
            "created_at": "2023-05-14T07:15:35.596171",
            "updated_at": "2023-05-14T07:15:35.596192",
            "place_id": "test_place_id",
            "user_id": "test_user_id",
            "text": "test_review_text",
            "__class__": "Review"
        }

    def tearDown(self):
        '''executed after each test'''
        pass

    def test_superclass_is_inherited(self):
        '''test if Review class inherits from BaseModel
        '''
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_attributes(self):
        '''test Review class attributes
        '''
        model = Review()
        self.assertTrue(hasattr(model, 'place_id'))
        self.assertTrue(hasattr(model, 'user_id'))
        self.assertTrue(hasattr(model, 'text'))

        self.assertEqual(model.place_id, '')
        self.assertEqual(model.user_id, '')
        self.assertEqual(model.text, '')

    def test_init_method(self):
        '''test__init__:
        test for constructor
        '''
        review = Review()
        self.assertEqual(type(review.id), str)
        self.assertEqual(type(review.created_at), datetime)
        self.assertEqual(type(review.updated_at), datetime)
        self.assertEqual(type(review.place_id), str)
        self.assertEqual(type(review.user_id), str)
        self.assertEqual(type(review.text), str)

    def test_str_method(self):
        '''test __str__ method string represntation
        '''
        model = Review()
        model_str = model.__str__()
        self.assertTrue('[Review]' in model_str)
        self.assertTrue('id' in model_str)
        self.assertTrue('created_at' in model_str)
        self.assertTrue('updated_at' in model_str)

    def test_to_dict_method(self):
        '''test to_dict method: obj dictionary reprr
        '''
        review = Review(**self.mock_data)
        review_dict = review.to_dict()
        self.assertEqual(review_dict['id'], 'test_id')
        self.assertEqual(review_dict['place_id'], 'test_place_id')
        self.assertEqual(review_dict['user_id'], 'test_user_id')
        self.assertEqual(review_dict['text'], 'test_review_text')
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertTrue('created_at' in review_dict)
        self.assertTrue('updated_at' in review_dict)
        self.assertEqual(type(review_dict['created_at']), str)
        self.assertEqual(type(review_dict['updated_at']), str)
        self.assertDictEqual(review.to_dict(), self.mock_data)

    def test_save_method(self):
        '''test_save_method:
        tes save method to persist to file
        '''
        review = Review()
        prev_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(prev_updated_at, review.updated_at)

    def test_empty_dict(self):
        '''empty_dict:
        test empty_dictionary instantiation
        '''
        model = Review({})
        self.assertEqual(model.place_id, '')
        self.assertEqual(model.user_id, '')
        self.assertEqual(model.text, '')

    def test_dtypes(self):
        '''test_attrs classes
        test attribute types
        '''
        model = Review()
        self.assertIsInstance(model.place_id, str)
        self.assertIsInstance(model.user_id, str)
        self.assertIsInstance(model.text, str)


if __name__ == '__main__':
    unittest.main()
