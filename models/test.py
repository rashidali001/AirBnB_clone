from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_user = User()
my_user.first_name = "Rashid"
my_user.last_name = "Bakari"
my_user.email = "airbnb2@mail.com"
my_user.password = "root"
my_user.save()

print(my_user)

