#!/usr/bin/python3
"""Interpreter of line commands
"""
from models import storage
from models.base_model import BaseModel
import models
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """This class contains the interpreter of commands"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """End of line: Exit the program"""
        return True

    def do_quit(self, line):
        """Quit: Exit the program"""
        return True

    def help_quit(self):
        """Help for command help_quit"""
        print("Quit command to exit the program")

    def emptyline(self):
        """Empty line + enter"""
        pass

    def do_create(self, args):
        """Create an instance of BaseModel

        Args:
            args (str): Class Name
        """
        line = args.split()
        if len(line) == 0:
            print("** class name missing **")
        elif globals().get(line[0]) is None:
            print("** class doesn't exist **")
        else:
            obj = eval(line[0])()
            obj.save()
            print("{}".format(obj.id))

if __name__ == '__main__':
    interpreter = HBNBCommand()
    interpreter.cmdloop()
