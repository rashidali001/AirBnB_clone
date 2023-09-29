"""File_storage - handles saving of the object instances,
    serialization and deseralization of saved instances
"""
#!/usr/bin/python3


import json
from models.base_model import BaseModel
from models.user import User

models = {
    "BaseModel":BaseModel,
    "User":User
}


class FileStorage():
    """Serializes instances to JSON file and
       deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = dict()


    def all(self):
        """ Returns __objects 
            syntax {"<classname>.<object.id>:{self.__dict__}"}
        """
        
        return self.__objects
    
    
    def new(self, obj):
        """ Sets in __objects the obj with key 
            <classname>.id
        """
        class_name = ""
        object_id = ""
        for key in obj:
            if key == "__class__":
                class_name = obj[key]
            if key == "id":
                object_id = obj[key]
        key = f"{class_name}.{object_id}"
        self.__objects[key] = obj

    
    def save(self):
        """Serializes __objects into __file_path
        """

        # Changes any object value -> to_dict()
        for key in self.__objects:
            if not isinstance(self.__objects[key], dict):
                self.__objects[key] = self.__objects[key].to_dict()
    

        with open(self.__file_path, "w") as file_storage:
            json.dump(self.__objects, file_storage)

    
    def reload(self):
        """Deserializes JSON file to __objects.
           If file is absent no exception should be raised
        """

        try:
            with open(self.__file_path, "r") as file_storage:
                self.__objects = json.load(file_storage)
                for key in self.__objects:
                    split_values = key.split(".")
                    class_name, object_id  = split_values 
                    for model in models:
                        if model == class_name:
                            self.__objects[key] = models[key](**self.__objects[key])                
                    # self.__objects[key] = BaseModel(**self.__objects[key])
                   
        except:
            pass


