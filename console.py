#!/usr/bin/python3
'''module: console - CLI interprter uses cmd module:
line-oriented command processor
hotwires command line interfaces in a program.
'''

import cmd

from models import storage
from models.base_model import BaseModel


PROMPT = '(hbnb) '

err_msg = ['** class name missing **',
           "** class doesn't exist **",
           '** instance id missing **',
           '** no instance found **',
           '** attribute name missing **',
           '** value missing **'
           ]

cls_names = {'BaseModel'}


class HBNBCommand(cmd.Cmd):
    '''HBNBCommand() - subclass of Cmd classs:
    shell for interacting with AirBnB objects,
    and to validate file storage
    '''
    prompt = PROMPT

    def do_create(self, arg):
        '''create
        creates a new instance of a class, saves it (to the JSON file)
        and prints the id.
        Ex: $ create BaseModel
        '''
        if not arg:
            print(err_msg[0])
            return
        try:
            cls = arg.split()[0]
            if cls not in cls_names:
                print(err_msg[1])
                return
            instance = eval(cls)()
            instance.save()
            print(instance.id)
        except Exception as e:
            pass

    def do_show(self, arg):
        '''show
        Prints the string representation of an instance based on the class
        name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        '''
        args = arg.split()
        if len(args) == 0:
            print(err_msg[0])
            return
        elif len(args) == 1:
            print(err_msg[2])
            return
        else:
            cls_name = args[0]
            obj_id = args[1]
            if cls_name not in cls_names:
                print(err_msg[1])
                return
            file_objs = storage.all()
            obj_key = f'{cls_name}.{obj_id}'
            if obj_key not in file_objs:
                print(err_msg[3])
                return
            print(file_objs[obj_key])

    def do_EOF(self, arg):
        '''EOF
        exit the interpreter with end-of-file SIGTERM ctrl + D
        or typing line 'EOF' in shell prompt
        '''
        print()
        return True

    def do_quit(self, arg):
        '''quit
        Quit command to exit the program
        type line chars 'quit'
        '''
        return True

    def emptyline(self):
        '''empty lines, or keyboard ENTER shouldn’t execute anything
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
