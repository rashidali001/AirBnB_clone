"""City class 
"""
#!/usr/bin/python3


from models.base_model import BaseModel


class City(BaseModel):
    """Two public attributes:
        + state_id (str)
        + name (str)
    """
    state_id = ""
    name = ""