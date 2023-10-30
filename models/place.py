<<<<<<< HEAD
"""Place class 
"""
#!/usr/bin/python3


=======
#!/usr/bin/python3
"""
Module Place class
"""
>>>>>>> a4eab4fe97dcd7aa475a83e3a1e8f3fcc24f3b3c
from models.base_model import BaseModel


class Place(BaseModel):
<<<<<<< HEAD
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
=======
    """
    Inherits from BaseModel
    Public class attributes:
        city_id:             (str) will be City.id
        user_id:             (str) will be User.id
        name:                (str)
        description:         (str)
        number_rooms:        (int) 0
        number_bathrooms:    (int) 0
        max_guest:           (int) 0
        price_by_night:      (int) 0
        latitude:            (float) 0.0
        longitude:           (float) 0.0
        amenity_ids:         (list) will be Amenity.id
>>>>>>> a4eab4fe97dcd7aa475a83e3a1e8f3fcc24f3b3c
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
<<<<<<< HEAD
    number_rooms = int()
    number_bathrooms = int()
    max_guests = int()
    price_by_night = int()
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = list()
    






    
=======
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
>>>>>>> a4eab4fe97dcd7aa475a83e3a1e8f3fcc24f3b3c
