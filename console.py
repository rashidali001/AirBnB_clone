<<<<<<< HEAD
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
=======
#!/usr/bin/python3
"""
Entry to command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Entry to command interpreter
    """
    prompt = "(hbnb) "
    classes = {"BaseModel", "State", "City",
               "Amenity", "Place", "Review", "User"}

    def do_EOF(self, line):
        """Exit on Ctrl-D"""
        print()
        return True

    def do_quit(self, line):
        """Exit on quit"""
        return True

    def emptyline(self):
        """Overwrite default behavior to repeat last cmd"""
        pass

    def do_create(self, line):
        """Create instance specified by user"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Print string representation: name and id"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """Destroy instance specified by user; Save changes to JSON file"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, line):
        """Print all objects or all objects of specified class"""
        args = parse(line)
        obj_list = []
        if len(line) == 0:
            for objs in storage.all().values():
                obj_list.append(objs)
            print(obj_list)
        elif args[0] in HBNBCommand.classes:
            for key, objs in storage.all().items():
                if args[0] in key:
                    obj_list.append(objs)
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update if given exact object, exact attribute"""
        args = parse(line)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            setattr(storage.all()[key], args[2], cast(arg3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def do_count(self, line):
        """Display count of instances specified"""
        if line in HBNBCommand.classes:
            count = 0
            for key, objs in storage.all().items():
                if line in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """Accepts class name followed by arguement"""
        args = line.split('.')
        class_arg = args[0]
        if len(args) == 1:
            print("*** Unknown syntax: {}".format(line))
            return
        try:
            args = args[1].split('(')
            command = args[0]
            if command == 'all':
                HBNBCommand.do_all(self, class_arg)
            elif command == 'count':
                HBNBCommand.do_count(self, class_arg)
            elif command == 'show':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip("'")
                id_arg = id_arg.strip('"')
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_show(self, arg)
            elif command == 'destroy':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip('"')
                id_arg = id_arg.strip("'")
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_destroy(self, arg)
            elif command == 'update':
                args = args[1].split(',')
                id_arg = args[0].strip("'")
                id_arg = id_arg.strip('"')
                name_arg = args[1].strip(',')
                val_arg = args[2]
                name_arg = name_arg.strip(' ')
                name_arg = name_arg.strip("'")
                name_arg = name_arg.strip('"')
                val_arg = val_arg.strip(' ')
                val_arg = val_arg.strip(')')
                arg = class_arg + ' ' + id_arg + ' ' + name_arg + ' ' + val_arg
                HBNBCommand.do_update(self, arg)
            else:
                print("*** Unknown syntax: {}".format(line))
        except IndexError:
            print("*** Unknown syntax: {}".format(line))


def parse(line):
    """Helper method to parse user typed input"""
    return tuple(line.split())


if __name__ == "__main__":
    HBNBCommand().cmdloop()
>>>>>>> a4eab4fe97dcd7aa475a83e3a1e8f3fcc24f3b3c
