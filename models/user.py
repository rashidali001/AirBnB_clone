"""User class that inherits Basemodel class
"""
#!/usr/bin/python3


from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
