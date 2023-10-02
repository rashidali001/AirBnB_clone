"""Review class 
"""
#!/usr/bin/python3


from models import base_model


class Review(base_model):
    """Three public attributes:
        + place_id (str)
        + user_id (str)
        + text (str)
    """
    place_id = ""
    user_id = ""
    text = ""