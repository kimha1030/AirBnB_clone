#!/usr/bin/python3
"""Interpreter of line commands
"""
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import cmd
import sys
import shlex


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
        """ Prints all string representation of all
            instances based or not on the class name.

        Args:
            args ([str]): Class name and id
        """
        my_list = []
        line = args.split()
        if len(line) > 0:
            if globals().get(line[0]) is None:
                print("** class doesn't exist **")
            else:
                my_dict = storage.all()
                for k, v in my_dict.items():
                    class_name = k.split(".", 1)
                    if line[0] == class_name[0]:
                        my_list.append(str(v))
                print(my_list)
        else:
            my_dict = storage.all()
            for k, v in my_dict.items():
                my_list.append(str(v))
            print(my_list)

    def do_update(self, args):
        """ Updates an instance based on the class
        name and id by adding or updating attribute

        Args:
            args ([str]): Class name and id
        """
        line = shlex.split(args)
        if len(line) == 0 or line[0] == "":
            print("** class name missing **")
        elif globals().get(line[0]) is None:
            print("** class doesn't exist **")
        elif len(line) == 1 or line[1] == "":
            print("** instance id missing **")
        elif len(line) == 2:
            my_dict = storage.all()
            key = line[0]+"."+line[1]
            if key not in my_dict:
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(line) == 3:
            print("** value missing **")
        else:
            my_dict = storage.all()
            key = line[0]+"."+line[1]
            if key in my_dict:
                setattr(my_dict[key], line[2], line[3])
                storage.save()
                print(my_dict[key])

if __name__ == '__main__':
    interpreter = HBNBCommand()
    interpreter.cmdloop()
