"""Command Interpreter processor {console}
"""
#!/usr/bin/python3


import cmd, sys
from models import BaseModel


class HBNBCommand(cmd.Cmd):
    """Airbnb command line processor
       Inherits from cmd.Cmd to make it a cmd line processor 
    """
    
    prompt = "(hbnb)"

    def do_quit(self, line):
        """ Exits the program """
        for arg in sys.argv:
            print(arg)

        return True
    
    def do_EOF(self, line):
        """ Exits the program """
        return True   
    

    def emptyline(self):
        """ Empty line? Pass (Do nothing) """
        pass



if __name__ == "__main__":
    HBNBCommand().cmdloop()