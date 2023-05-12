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
        except Exception:
            pass

    def do_show(self, arg):
        '''show
        prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        '''
        args = arg.split()

        if len(args) == 0:
            print(err_msg[0])
        elif len(args) == 1:
            if args[0] not in cls_names:
                print(err_msg[1])
            else:
                print(err_msg[2])
        elif len(args) == 2 and args[0] not in cls_names:
            print(err_msg[1])
        else:
            obj_key = f'{args[0]}.{args[1]}'
            file_objs = storage.all()
            if obj_key not in file_objs:
                print(err_msg[3])
                return
            print(file_objs[obj_key])

    def do_destroy(self, arg):
        '''destroy
        deletes an instance based on the class name
        and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        '''
        args = arg.split()

        if len(args) == 0:
            print(err_msg[0])
        elif args[0] not in cls_names:
            print(err_msg[1])
        elif len(args) == 1:
            print(err_msg[2])
        else:
            obj_key = f'{args[0]}.{args[1]}'
            file_objs = storage.all()
            if obj_key not in file_objs:
                print(err_msg[3])
                return
            del file_objs[obj_key]
            storage.save()

    def do_all(self, arg):
        '''all
        prints all string representation of all instances
        based or not on the class name.
        ex: $ all BaseModel or $ all.
        '''
        if not arg:
            print([str(file_obj) for file_obj in storage.all().values()])
            return

        else:
            try:
                cls = arg.split()[0]

                if cls not in cls_names:
                    print(err_msg[1])
                    return
                print([str(obj) for obj in storage.all(cls).values()])
            except Exception:
                pass

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
