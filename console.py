#!/usr/bin/python3
'''
console module - We will be implementing a command line interpreter
we are going to import the cmd module
'''


import cmd


class HBNBCommand(cmd.Cmd):
    ''' Implementing the HBNBCommand class'''

    prompt = '(hbnb) '

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
