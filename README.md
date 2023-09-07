
-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------

The Airbnb_clone (The console) insists of the creation of a command line interpreter
that will be used to dispatch commands written by the user to their respective methods
in the program.


-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------

We are going to create a parent class (BaseModel) that will handle initialization, serialization
and, deserialization of future object instances

After the creation of the base class, we are going to create classes that will inherit the  
BaseModel class

-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------

The command interpreter is started when running the main script and making sure it doesn't 
work when imported by using ( if name == "main" ) to start the script

It's usage is by writing the commands on the console that are available in the command 
interpreter. You can use " help {command} " to check how a specific command is being
used.

Example:

        (hbnb) help

        Documented commands (type help <topic>)
        ---------------------------------------

        EOF help quit



