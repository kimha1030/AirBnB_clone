#!/usr/bin/python3
"""Base Model class
"""
import models
import json
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ [Class BaseModel]
    """

    def __init__(self, *args, **kwargs):
        """ [Constructor of class]
        """
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "created_at":
                    self.__dict__[k] =\
                     datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "updated_at":
                    self.__dict__[k] =\
                     datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif k != "__class__":
                        setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """ This method print the
            str representation
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """ This method updates "updated_at"
            with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ This method return a dict that
            contains the class attributes
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
