"""Command Interpreter processor {console}
"""
#!/usr/bin/python3


import cmd, datetime
from models.base_model import BaseModel
from models.user import User
from models import storage

Models = {
    "basemodel" : BaseModel,
    "user":User
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
                        obj = value_m(value_o)
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
                            print(value_a.__dict__)
                            print(type(value_a.__dict__["created_at"]))
                            print(type(value_a.__dict__["updated_at"]))
                            obj = Models[key](**value_a.__dict__)
                            print(obj)
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
    
    def do_reload(self, line):
        storage.reload()
        all_objects = storage.all()

    def do_quit(self, line):
        """ Exits the program """
        return True
    
    def do_EOF(self, line):
        """ Exits the program """
        return True   
    

    def emptyline(self):
        """ Empty line? Pass (Do nothing) """
        pass



if __name__ == "__main__":
    HBNBCommand().cmdloop()