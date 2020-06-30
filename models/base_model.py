#!/usr/bin/python3
"""Base class
"""
from uuid import uuid4
from datetime import datetime
import models
import json


class BaseModel():
    """ [Class BaseModel]
    """
    def __init__(self, *args, **kwargs):
        """ [Constructor of class]
        """
        if kwargs or len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "create_at":
                    self.__dict__[k] =\
                     datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "update_at":
                    self.__dict__[k] =\
                     datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                        if k != "__class__":
                            setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
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
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ This method return a dict that
            contains the class attributes
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        for k, v in new_dict.items():
            if isinstance(v, datetime):
                new_dict[k] = v.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return new_dict
