#!/usr/bin/python3
'''
console module - We will be implementing a command line interpreter
we are going to import the cmd module
'''


import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    ''' Implementing the HBNBCommand class'''

    prompt = '(hbnb) '
    __class_names = {'BaseModel': BaseModel}

    def do_create(self, arg):
        '''Creates a new Instance of a specified file.
        synatx is : create BaseModel'''
        if not arg:
            print("** class name missing **")
            return False
        if arg not in HBNBCommand.__class_names.keys():
            print("** class doesn't exist **")
            return False

        for key, value in HBNBCommand.__class_names.items():
            if key == arg:
                new_instance = value()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, arg):
        ''' Prints the string representation of
        an instance based on the class name
        synatx: show BaseModel 1234-1234-1234
        '''
        if not arg:
            print("** class name missing **")
            return False

        arg = arg.split(" ")

        if arg[0] not in HBNBCommand.__class_names.keys():
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False

        obj_to_find = str(arg[0]) + "." + str(arg[1])

        storage.reload()
        all_objects = storage.all()

        for key, value in all_objects.items():
            if key == obj_to_find:
                print(value)
                return False

        print('** no instance found **')
        return False

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id
        synatx: destroy BaseModel 1234-1234-1234'''
        if not arg:
            print("** class name missing **")
            return False

        arg = arg.split(" ")

        if arg[0] not in HBNBCommand.__class_names.keys():
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False

        obj_to_find = str(arg[0]) + "." + str(arg[1])

        storage.reload()
        all_objects = storage.all()

        for key in all_objects.keys():
            if key == obj_to_find:
                del all_objects[key]
                storage.save()
                return False

        print("** no instance found **")
        return False

    def do_all(self, arg):
        ''' Prints all string representation of all
        instances based or not on the class name.
        synatx: all BaseModel or all'''

        if not arg:
            storage.reload()
            all_objects = storage.all()
            general = list()
            for key, value in all_objects.items():
                general.append(str(value))
            print(general)
            return False

        arg = arg.split(" ")

        if arg[0] not in HBNBCommand.__class_names.keys():
            print("** class doesn't exist **")
            return False

        storage.reload()
        all_objects = storage.all()
        general = list()
        for key, value in all_objects.items():
            name, id = key.split(".")
            if name == arg[0]:
                general.append(str(value))

        print(general)
        return False

    def do_update(self, arg):
        ''' Updates an instance based on the class name and id
        usage: update <class name> <id> <attribute name> "<attribute value>"'''

        if not arg:
            print("** class name missing **")
            return False

        arg = arg.split(" ")

        if arg[0] not in HBNBCommand.__class_names.keys():
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False

        obj_to_find = str(arg[0]) + "." + str(arg[1])

        storage.reload()
        all_objects = storage.all()

        if obj_to_find not in all_objects.keys():
            print("** no instance found **")
            return False

        if len(arg) == 2:
            print("** attribute name missing **")
            return False

        if len(arg) == 3:
            print("** value missing **")
            return False

        if arg[2] == "id" or arg[2] == "created_at" or arg[2] == "updated_at":
            print("{} can't be updated!".format(arg[2]))
            return False

        for key, value in all_objects.items():
            if key == obj_to_find:
                dict_repr = value.to_dict()
                # using strip to remove the double quotation marks
                dict_repr.update({arg[2]: arg[3].strip('\"')})
                obj_update = BaseModel(**dict_repr)
                all_objects[key] = obj_update
                storage.save()

    def do_quit(self, arg):
        '''Quit command to exit program'''
        raise SystemExit

    def do_EOF(self, arg):
        '''End of File'''
        raise SystemExit

    # overriding the emptyline method in cmd.Cmd
    def emptyline(self):
        '''Makes sure nothing is executed'''
        pass

    def help_quit(self):
        '''Gives a documentantion about quit'''
        print("Quit command to exit program\n")

    def help_EOF(self):
        '''Gives a documentantion about EOF (End of File)'''
        print("EOF command to exit program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
