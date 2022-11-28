#!/usr/bin/python3
'''
file_storage module
-> private class attribute:
    -> __file_path: string - path to the json file
    -> __objects: dictionary - empty but
        will store all objects by <class name>.id
-> public instance methods:
    -> all(self): retuns th dictionary __objects
    -> new(self, obj): sets in __objects the obj with key
        <obj class name>.id
    ->save(self): serializes __objects to the json file path
    ->reload(self): deserializes the json file to __objects
'''


import json
from datetime import datetime
from os.path import exists
from models.base_model import BaseModel


class FileStorage():
    ''' FileStorage class '''

    # private class attributes
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        '''Returns the dictionary __object'''
        return FileStorage.__objects

    def new(self, obj):
        '''Sets in __object the obj with key <obj class name>.id'''

        key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        '''serializes __objects to the json file'''

        '''
        First in the loop:
        we take all the values which we had coverted
        from dictionaries to objects when loading them
        in the reload function and converting them
        back to dictionaries so that we can be able to
        store them in the file.json
        '''
        for key, value in FileStorage.__objects.items():
            if not isinstance(value, dict):
                FileStorage.__objects[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        '''Deserializes the json file to __objects'''
        file_exist = exists(FileStorage.__file_path)
        if file_exist is True:
            with open(FileStorage.__file_path, 'r') as file:
                FileStorage.__objects = json.load(file)
                for key, value in FileStorage.__objects.items():
                    FileStorage.__objects[key] = BaseModel(**value)
