<<<<<<< HEAD
"""Review class 
"""
#!/usr/bin/python3


=======
#!/usr/bin/python3
"""
Module Review class
"""
>>>>>>> a4eab4fe97dcd7aa475a83e3a1e8f3fcc24f3b3c
from models.base_model import BaseModel


class Review(BaseModel):
<<<<<<< HEAD
    """Three public attributes:
        + place_id (str)
        + user_id (str)
        + text (str)
    """
    place_id = ""
    user_id = ""
    text = ""
=======
    """
    Inherits from BaseModel
    Public class attributes:
        place_id:            (str) will be Place.id
        user_id:             (str) will be User.id
        text:                (str)
    """
    place_id = ""
    user_id = ""
    text = ""
>>>>>>> a4eab4fe97dcd7aa475a83e3a1e8f3fcc24f3b3c
