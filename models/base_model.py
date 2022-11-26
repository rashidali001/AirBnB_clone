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

                      -> an extra key called __class__ is added with the value being the
                         class name of the object

                      -> converts "created_at" and  "updated_at" to string object in ISO fromat

                      -> This method will be the first piece of the serialization/deserialization
                         process

                      -> In Summary: the method creates a dictionary representation with
                                     "simple object type" of our BaseModel class
'''


from datetime import datetime
import uuid

class BaseModel():
    '''BaseModel class'''

    def __init__(self):
        '''Initializing object...'''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''String representation of object'''

        print(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        '''Updates the time object was changed'''

        self.updated_at = datetime.now()

    def to_dict(self):
        pass


