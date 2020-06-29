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

    def do_show(self, args):
        """ Prints the string representation of an instance
            based on the class name and id

        Args:
            args ([str]): Class name and id
        """
        line = args.split()
        if len(line) == 0:
            print("** class name missing **")
        elif globals().get(line[0]) is None:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            my_dict = storage.all()
            key = line[0]+"."+line[1]
            if key in my_dict:
                print(my_dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """  Deletes an instance based on the class name
             and id (save the change into the JSON file)

        Args:
            args ([str]): Class name and id
        """
        line = args.split()
        if len(line) == 0:
            print("** class name missing **")
        elif globals().get(line[0]) is None:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            my_dict = storage.all()
            key = line[0]+"."+line[1]
            if key in my_dict:
                    del my_dict[key]
                    storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        my_list = []
        line = args.split()
        if len(line) > 0:
            if globals().get(line[0]) is None:
                print("** class doesn't exist **")
            else:
                my_dict = storage.all()
                for  k, v in my_dict.items:
                    



if __name__ == '__main__':
    interpreter = HBNBCommand()
    interpreter.cmdloop()
