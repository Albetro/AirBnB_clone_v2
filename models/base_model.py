#!/usr/bin/python3
""""Defines the BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project"""

    def __init__(self, *args, **kwargs):
        """Initializes the Base Model"""
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or m == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, tformat)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)

    def save(self):
        """Updates update_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """"Return the dictionary of the BaseModel instance"""
        ndict = self.__dict__.copy()
        ndict["created_at"] = self.created_at.isoformat()
        ndict["updated_at"] = self.updated_at.isoformat()
        ndict["__class__"] = self.__class__.__name__
        return ndict

    def __str__(self):
        """Returns the print/str representation of the BaseModel instance"""
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
