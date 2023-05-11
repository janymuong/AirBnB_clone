#!/usr/bin/python3
'''module: console - CLI interprter uses cmd module:
line-oriented command processor
hotwires command line interfaces in a program.
'''

import cmd

PROMPT = '(hbnb) '


class HBNBCommand(cmd.Cmd):
    '''HBNBCommand() - subclass of Cmd classs:
    shell for interacting with AirBnB objects,
    and to validate file storage
    '''
    prompt = PROMPT

    def do_EOF(self, line):
        '''EOF
        exit the interpreter with keybaorad interrupt ctrl + D
        or typing line 'EOF'
        '''
        print()
        return True

    def do_quit(self, line):
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
