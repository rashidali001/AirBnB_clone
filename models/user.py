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
    email = ""
    password = ""
    first_name = ""
    last_name = ""
