#!/usr/bin/python3
'''
test_base_model

We are going to use this module to test our base_model module
'''


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''TestBaseModel'''

    def test_classname(self):
        '''Testing if the object is of BaseModel class'''
        obj = BaseModel()
        self.assertEqual(obj.__class__.__name__, 'BaseModel')

    def test_id_present(self):
        '''Testing if the object has an id'''
        obj = BaseModel()
        self.assertTrue(obj.id)

    def test_created_at_present(self):
        '''Testing if object has a created at date'''
        obj = BaseModel()
        self.assertTrue(obj.created_at)

    def test_updated_at_present(self):
        '''Testing if object has a created at date'''
        obj = BaseModel()
        self.assertTrue(obj.updated_at)

    def test_to_dict(self):
        '''Testing if to_dict returns a dictionary'''
        obj = BaseModel()
        self.assertIsInstance(obj.to_dict(), dict)

    def test_other_sequence(self):
        with self.assertRaises(TypeError):
            arg = [1, 3, 4]
            obj = BaseModel(**arg)
