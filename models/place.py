"""Place class 
"""
#!/usr/bin/python3


from models.base_model import BaseModel


class Place(BaseModel):
    """Eleven public attributes:
        + city_id (str)
        + user_id (str)
        + name (str)
        + description (str)
        + number_rooms (int)
        + number_bathrooms (int)
        + max_guests (int)
        + price_by_night (int)
        + latitude (float)
        + longitude (float)
        + amenity_ids (list)
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = int()
    number_bathrooms = int()
    max_guests = int()
    price_by_night = int()
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = list()
    






    