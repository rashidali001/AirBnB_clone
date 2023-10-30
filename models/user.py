<<<<<<< HEAD
"""User class that inherits Basemodel class
"""
#!/usr/bin/python3


from models.base_model import BaseModel


class User(BaseModel):
    """Four public atrribute:
        + first_name (str)
        + last_name (str)
        + email (str)
        + password (str)
    """
=======
#!/usr/bin/python3
"""user class
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    '''base model class'''

>>>>>>> a4eab4fe97dcd7aa475a83e3a1e8f3fcc24f3b3c
    email = ""
    password = ""
    first_name = ""
    last_name = ""
