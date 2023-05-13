#!/usr/bin/python3
'''module: console - CLI interprter uses cmd module:
line-oriented command processor
hotwires command line interfaces in a program.
'''

import cmd

from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


PROMPT = '(hbnb) '

err_msg = ['** class name missing **',
           "** class doesn't exist **",
           '** instance id missing **',
           '** no instance found **',
           '** attribute name missing **',
           '** value missing **'
           ]

cls_names = {'BaseModel', 'User', 'Place', 'State', 'City',
             'Amenity', 'Review'}


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

    def do_update(self, arg):
        '''update
        updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        usage: update <class name> <id> <attribute name> "<attribute value>"
        '''
        args = arg.split()

        if not arg:
            print(err_msg[0])
            return
        if args[0] not in cls_names:
            print(err_msg[1])
            return
        if len(args) < 2:
            print(err_msg[2])
            return

        file_objs = storage.all()
        obj_key = f'{args[0]}.{args[1]}'
        if obj_key not in file_objs:
            print(err_msg[3])
            return

        obj = file_objs[obj_key]

        if len(args) == 2:
            print(err_msg[4])
            return
        if len(args) < 4:
            print(err_msg[5])
            return

        attr = args[2]
        value = args[3]

        if not hasattr(obj, attr):
            print("** errmsg: attribute not found **")
            return
        elif attr == 'id' or attr == 'created_at' or attr == 'updated_at':
            return
        try:
            value = type(getattr(obj, attr))(value)
        except ValueError:
            pass
        setattr(obj, attr, value)
        storage.save()
        return

    def do_all(self, arg):
        '''all
        prints all string representation of all instances
        based or not on the class name.
        ex: $ all BaseModel or $ all.
        '''
        if not arg:
            print([str(file_obj) for file_obj in storage.all().values()])
            return

        try:
            cls = arg.split()[0]

            if cls not in cls_names:
                print(err_msg[1])
                return
            file_objs = storage.all()
            print([str(obj) for obj in file_objs.values()
                   if obj.__class__.__name__ == cls])
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
