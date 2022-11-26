#!/usr/bin/python3
'''
base_model module

-> public instance attributes:
    -> id
    -> created_at
    -> updated_at

-> __str__:
    -> Should print: [<class name>] (<self.id>) <self.__dict__>

-> public instance methods:
    -> save(self): updates the attribute "updated_at" with current date time
    -> to_dict(self): returns a dictionary representation of the created object
                      containing all keys/values of __dict__ of the instance

                      -> an extra key called __class__ is added with the
                      value being the class name of the object

                      -> converts "created_at" and  "updated_at" to
                      string object in ISO format

                      -> This method will be the first piece of the
                      serialization/deserialization process

                      -> In Summary: the method creates a dictionary
                      representation with "simple object type"
                      of our BaseModel class
'''


from datetime import datetime
import uuid
import json
from models import storage


class BaseModel():
    '''
    BaseModel class
    '''

    def __init__(self, *args, **kwargs):
        '''Initializing object...'''

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                # strptime(value, format) - to convert a string to datetime
                if key == "__class__":
                    continue

                if key == "created_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

                if key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''String representation of object'''

        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        '''Updates the time object was changed'''

        self.updated_at = datetime.now()
        self.updated_at = str(self.updated_at.isoformat())
        storage.save()

    def to_dict(self):
        '''Returns a dictionary'''

        dict_repr = dict()
        dict_repr = self.__dict__
        dict_repr['__class__'] = self.__class__.__name__
        dict_repr['created_at'] = str(self.created_at.isoformat())
        dict_repr['updated_at'] = str(self.updated_at.isoformat())

        return dict_repr
