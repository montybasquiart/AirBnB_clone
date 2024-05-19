#!/usr/bin/python3
"""
    The file storage module
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
        This module handles file storage
    """
    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        """
            Returns the "__objects" dictionary
        """
        return self.__objects

    def new(self, obj):
        """
            Sets in "__objects" the "obj" with key "<obj class_name>.id"
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
            Serialize "__objects" and save to json file (path: __file_path)
        """
        obj_dict = {}

        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
            Deserialize the json file to "__objects" only if
            "__file_path" exists. Otherwise, do nothing
        """
        try:
            with open(self.__file_path, 'r') as f:
                dict_obj = json.load(f)
            for key, value in dict_obj.items():
                val = self.class_dict[value['__class__']](**value)
                self.__objects[key] = val
        except FileNotFoundError:
            pass
