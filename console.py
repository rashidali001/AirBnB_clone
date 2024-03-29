"""Command Interpreter processor {console}
"""
#!/usr/bin/python3


import cmd, datetime
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage

Models = {
    "basemodel" : BaseModel,
    "user":User,
    "amenity":Amenity,
    "city":City,
    "place":Place,
    "review":Review,
    "state":State
}


class HBNBCommand(cmd.Cmd):
    """Airbnb command line processor
       Inherits from cmd.Cmd to make it a cmd line processor 
    """
    
    prompt = "(hbnb)"

    def do_create(self, line):
        """creates a new instance of a model class
            Usage: create <class name>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        
        model_name = args[0].lower()
        if not model_name in Models:
            print("** class doesn't exist **")
            return
        

        count = 1
        while (count < len(args)):     
            
        
            split_values = args[count].split("=")
            bf_equals, af_equals = split_values

            if '"' in af_equals:
                value = af_equals.strip('"')
                if '_' in value:
                    value = value.replace('_', ' ')
                





        new_object = Models[model_name]()
        new_object.save()
        print (f"{new_object.__class__.__name__} {new_object.id}")      


    def do_show(self, line):
        """Prints a string representative of an instance
           based on classname & id
           Usage:
           show <classname> 
           or
           show <classname> <object id>
           Ex results: 
           BaseModel 32090290djh-329393
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        
        model_name = args[0].lower()
        if not model_name in Models:
            print("** class doesn't exist **")
            return
        
        if len(args) == 1:
            all_objects = storage.all()
            for key in all_objects.keys():
                """Spliting BaseModel.12567 into
                    arg1 = BaseModel
                    arg2 = 12567
                """
                split_values = key.split(".")
                class_name, object_id = split_values
                class_name_lower = class_name.lower()
                if class_name_lower == model_name:
                    print(f"{class_name} {object_id}")

                
            return
        
        if len(args) == 2:
            arg_id = args[1]
            all_objects = storage.all()
            for key in all_objects.keys():
                """Spliting BaseModel.12567 into
                    arg1 = BaseModel
                    arg2 = 12567
                """
                split_values = key.split(".")
                class_name, object_id = split_values
                if arg_id == object_id:
                    print(f"{class_name} {object_id}")
                    return
            
        print("** no instance found **")

    
    def do_destroy(self, line):
        """Deletes an instance based on the specified class name and object id
           Usage:
           destroy <classname> <object id>
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        
        model_name = args[0].lower()
        if not model_name in Models:
            print("** class doesn't exist **")
            return
        
        if len(args) == 1:
            print("** instance id missing **")
            return
        
        if len(args) == 2:
            arg_id = args[1]
            all_objects = storage.all()
            for key in all_objects.keys():
                """Spliting BaseModel.12567 into
                    arg1 = BaseModel
                    arg2 = 12567
                """
                split_values = key.split(".")
                class_name, object_id = split_values
                if arg_id == object_id:
                    all_objects.pop(key) # Destroying the object specified   
                    storage.__objects = all_objects
                    storage.save()
                    return
                
        print("** no instance found **")
    
    def do_all(self, line):
        """Prints all string representation of all instances
           based or not on the class name
           Usage: all / all <classname>
        """
        result = list()
        args = line.split()


        all_objects = storage.all()
        
        if len(args) > 1:
            print(" ** Invalid syantax **")
            print(" ** Usage: all / all <classname> **")
            return

        if len(args) == 1:
            class_name_arg = args[0].lower()
            if not class_name_arg in Models:
                print("** class doesn't exist **")
                return

            for key_o, value_o in all_objects.items():
                split_values = key_o.split(".")
                class_name_o, object_id_o = split_values
                class_name_o = class_name_o.lower()
                for key_m, value_m in Models.items():
                    if key_m == class_name_arg:
                        if class_name_o == class_name_arg:
                             obj = value_m(**value_o)
                             result.append(f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}")
            
            print(result)
            return                             



        for key in all_objects.keys():
            split_values = key.split(".")
            class_name, object_id = split_values
            class_name = class_name.lower()
            for model_name in Models:
                if class_name == model_name:
                    obj = Models[model_name](**all_objects[key]) # suppose to be **all_objects[key]
                    result.append(f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}")
        
        print(result)
    

    def do_update(self,line):
        """Updates an instance based on the class name and id by adding or
           updating attribute (save the change into the JSON file).
           Usage:
           update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()
        updated_object = None

        if len(args) == 0:
            print("** class name missing **")
            return
        
        class_name_arg = args[0].lower()

        if not class_name_arg in Models:
            print("** class doesn't exist **")
            return
        
        if len(args) == 1:
            print("** instance id missing **")
            return
        
        arg_id = args[1]
        all_objects = storage.all()
        class_objects_id = list()


        for key in all_objects:
            split_values = key.split(".")
            class_name, object_id = split_values
            class_name = class_name.lower()
            if class_name_arg == class_name:
                class_objects_id.append(object_id)
        
        if not arg_id in class_objects_id:
            print("** no instance found **")
            return
        
        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return
        
        attribute_name = args[2]
        attribute_value = args[3]

        if args[3][0] == "'" or args[3][0] == '"':
            attribute_value = args[3][1:-1]

        

        for key in Models:
            if key == class_name_arg:
                for key_a, value_a in all_objects.items():
                    split_values = key_a.split(".")
                    class_name, object_id = split_values
                    class_name = class_name.lower()
                    if class_name == class_name_arg:
                        if object_id == arg_id:
                            obj = Models[key](**value_a)
                            setattr(obj, attribute_name, attribute_value)
                            obj.updated()
                            updated_object = obj
        
        for key in all_objects:
            split_values = key.split(".")
            class_name, object_id = split_values
            class_name = class_name.lower()
            if class_name == class_name_arg:
                if object_id == arg_id:
                    all_objects[key] = updated_object
        
        """
        for key in all_objects:
            split_values = key.split(".")
            class_name, object_id = split_values
            class_name = class_name.lower()
            if class_name_arg == class_name:
                if arg_id == object_id:
                    obj = all_objects[key]
                    setattr(obj, attribute_name, attribute_value)
                    obj.updated()
                    all_objects[key] = obj   
        """     
        
        storage.__objects = all_objects
        storage.save()
        storage.reload()                   
        
    """
    def do_reload(self, line):
        storage.reload()
        all_objects = storage.all()
    """

    def default(self, line):
        args = line.split(".")
        arg1 = args[0].lower() # arg1 - classname
        if arg1 in Models:
            arg2 = args[1].split("(")[0] # arg2 - method / property
            if arg2 == "all":
                HBNBCommand.do_all(self, arg1)

            if arg2 == "count":
                count = 0
                all_objects = storage.all()
                for key in all_objects:
                    split_values = key.split(".")
                    class_name, object_rep = split_values
                    if class_name.lower() == arg1:
                        count += 1
                print(count)
                return
            
            if arg2 == "show":
               id = args[1].split('"')[1]
               all_objects = storage.all()
               for key, value in all_objects.items():
                   split_values = key.split(".")
                   class_name, object_id = split_values
                   if object_id == id:
                       for key in Models:
                           if key == class_name.lower():
                                obj = Models[key](**value)
                                print(obj)
                                return
               print("** no instance found **")

            if arg2 == "destroy":
                id = args[1].split('"')[1]
                all_objects = storage.all()
                for key in all_objects.keys():
                    """Spliting BaseModel.12567 into
                        arg1 = BaseModel
                        arg2 = 12567
                    """
                    split_values = key.split(".")
                    class_name, object_id = split_values
                    if id == object_id:
                        all_objects.pop(key) # Destroying the object specified   
                        storage.__objects = all_objects
                        storage.save()
                        return
                    
                print("** no instance found **")
            
            if arg2 == "update":
                id = args[1].split('"')[1]
                # Ex: arguments - # ['"f26bc3d7-75c2-4c01-b974-056c01a35227"', ' "first_name"', ' "john"']
                # Ex: arguments - # ['"f26bc3d7-75c2-4c01-b974-056c01a35227"', {'first_name':"Betty"}]
                arguments = args[1][6:].strip("()").split(",") 
                property_arg = arguments[1].strip(" ").strip('"')
                value_arg = arguments[2].strip(" ")
                if '"' not in value_arg:
                    value_arg = int(value_arg) 
                
                if type(value_arg) == str:
                    value_arg = value_arg.strip('"')
                
                if "{" in arguments[1]:
                    print("Dictionaries are not applicable at the moment")
                    return

                all_objects = storage.all()
                for key, value in all_objects.items():
                    split_values = key.split(".")
                    class_name, object_id = split_values
                    class_name = class_name.lower()
                    if id == object_id:
                        for model in Models:
                            if model == arg1:
                                obj = Models[model](**value)
                                setattr(obj, property_arg, value_arg)
                                obj.updated()
                                all_objects[key] = obj
                                storage.__objects = all_objects
                                storage.save()
                                storage.reload()       
                                return                 

                print("** no instance found **")   



                
               
                
                                   
                
                    
                    
                       
                       

            
                
                
            

        

    def do_quit(self, line):
        """ Exits the program """
        return True
    
    def do_EOF(self, line):
        """ Exits the program """
        return True   
    

    def emptyline(self):
        """ Empty line? Pass (Do nothing) """
        pass
    """
    Testing purposes
    """
    def do_testCreate(self, arg):
            
      pass



if __name__ == "__main__":
    HBNBCommand().cmdloop()