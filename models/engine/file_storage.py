"""File_storage - handles saving of the object instances,
    serialization and deseralization of saved instances
"""
#!/usr/bin/python3


import json


class FileStorage():
    """Serializes instances to JSON file and
       deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = dict()


    def all(self):
        """ Returns __objects """
        
        return self.__objects
    
    
    def new(self, obj):
        """ Sets in __objects the obj with key 
            <classname>.id
        """

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    
    def save(self):
        """Serializes __objects into __file_path
        """

        with open(self.__file_path, "w") as file_storage:
            json.dump(self.__objects, file_storage)
    
    def reload(self):
        """Deserializes JSON file to __objects.
           If file is absent no exception should be raised
        """

        try:
            with open(self.__file_path, "r") as file_storage:
                self.__objects = json.load(file_storage)
        except:
            pass


