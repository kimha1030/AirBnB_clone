#!/usr/bin/python3
"""Base class
"""
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel():
    """ [Class BaseModel]
    """
    def __init__(self, *args, **kwargs):
        """ [Constructor of class]
        """
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            #storage.new(self)
        else:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
            self.__dict__["created_at"] =\
            datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__["updated_at"] =\
            datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """ This method print the
            str representation
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """This method save the current date of update
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """This method return a dict
        """
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__
