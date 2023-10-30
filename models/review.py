"""Review class 
"""
#!/usr/bin/python3


from models.base_model import BaseModel


class Review(BaseModel):
    """Three public attributes:
        + place_id (str)
        + user_id (str)
        + text (str)
    """
    place_id = ""
    user_id = ""
    text = ""