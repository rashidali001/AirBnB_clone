<<<<<<< HEAD
"""Script handling all the unit tests that base_model.py is going 
    to have
"""
#!/usr/bin/python3


from models.base_model import BaseModel
import unittest

=======
#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
import os
import pep8
from models.base_model import BaseModel
>>>>>>> a4eab4fe97dcd7aa475a83e3a1e8f3fcc24f3b3c


class TestBaseModel(unittest.TestCase):

<<<<<<< HEAD
    def test_str_representation(self):
        obj = BaseModel()
        self.assertTrue(type(print(obj)), str)

=======
    @classmethod
    def setUpClass(cls):
        cls.base1 = BaseModel()
        cls.base1.name = "Greg"
        cls.base1.my_number = 29

    @classmethod
    def tearDownClass(cls):
        del cls.base1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_functions(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        self.assertTrue(isinstance(self.base1, BaseModel))

    def test_save(self):
        self.base1.save()
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)

    def test_to_dict(self):
        base1_dict = self.base1.to_dict()
        self.assertEqual(self.base1.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base1_dict['created_at'], str)
        self.assertIsInstance(base1_dict['updated_at'], str)
>>>>>>> a4eab4fe97dcd7aa475a83e3a1e8f3fcc24f3b3c


if __name__ == "__main__":
    unittest.main()
