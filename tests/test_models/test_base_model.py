"""Script handling all the unit tests that base_model.py is going 
    to have
"""
#!/usr/bin/python3


from models.base_model import BaseModel
import unittest



class TestBaseModel(unittest.TestCase):

    def test_str_representation(self):
        obj = BaseModel()
        self.assertTrue(type(print(obj)), str)



if __name__ == "__main__":
    unittest.main()
