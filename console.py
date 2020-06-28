#!/usr/bin/python3
"""Interpreter of line commands
"""
from models import storage
import cmd


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

if __name__ == '__main__':
    interpreter = HBNBCommand()
    interpreter.cmdloop()
