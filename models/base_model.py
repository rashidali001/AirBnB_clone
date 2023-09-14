""" BaseModel class creation responsible of initialization
    serialization and deserialization of future instances
"""
#!/usr/bin/python3


from datetime import datetime
import uuid


obj_is_new = False

class BaseModel():
    """ Creating attributes and methods for the parent class """

    def __init__(self, *args, **kwargs):
        
        if kwargs.__len__() != 0:
            print("here")
            """ Initialization of dict objects is kwargs is not empty"""
            for key, value in kwargs.items():
                if key  == "__class__":
                    continue


                # Converting date strings to date objects

                if key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                    continue

                if key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                    continue

                setattr(self, key, value)
            
        else:
            """ Default initialization process """
            global obj_is_new
            obj_is_new = True
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        
        
        

    def __str__(self):
        """ Prints a string representation of an specific object instance """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    
    def save(self):
        """ updates the time to the current one when changes are made """
        from models import storage
        global obj_is_new
        if (obj_is_new):
            storage.new(self.to_dict())
        storage.save()



    def to_dict(self):
        """ Returning a dictionary containing all
            key/values
        """
        obj_dict = self.__dict__
        obj_dict["__class__"] = self.__class__.__name__
        # Converting the date objects to string
        obj_dict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f") 
        obj_dict["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return obj_dict
    