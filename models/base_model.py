<<<<<<< HEAD
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
            """ Initialization of dict objects is kwargs is not empty"""
            for key, value in kwargs.items():
                if key  == "__class__":
                    continue


                # Converting date strings to date objects


                if (key == "created_at")and not isinstance(value, datetime):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                    continue

                if (key == "updated_at") and not isinstance(value, datetime):
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
    
    def updated(self):
        self.updated_at = datetime.now()



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
    
=======
#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models

"""
Module BaseModel
Parent of all classes
"""


class BaseModel():
    """Base class for Airbnb clone project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes: random uuid, dates created/updated


        """
        if kwargs:
            for key, val in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return string of info about model
        """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """
        returns string representation
        """
        return (self.__str__())

    def save(self):
        """
        Update instance with updated time & save to serialized file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dic with string formats of times; add class info to dic
        """
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic
>>>>>>> a4eab4fe97dcd7aa475a83e3a1e8f3fcc24f3b3c
