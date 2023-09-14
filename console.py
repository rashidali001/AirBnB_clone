"""Command Interpreter processor {console}
"""
#!/usr/bin/python3


import cmd
from models.base_model import BaseModel
from models import storage

Models = {
    "basemodel" : BaseModel
}


class HBNBCommand(cmd.Cmd):
    """Airbnb command line processor
       Inherits from cmd.Cmd to make it a cmd line processor 
    """
    
    prompt = "(hbnb)"

    def do_create(self, line):
        """creates a new instance of a model class
            syntax: create <class name>
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