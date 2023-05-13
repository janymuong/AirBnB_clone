#!/usr/bin/python3
'''module: file_storage
a module that serializes instances to a JSON file
and deserializes JSON file to instances.
'''

import json

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    '''a class that serializes instances to a JSON file
    and deserializes JSON file to instances.

    attributes:
        __file_path: relative path to json file
        __objects: initially empty - returns the dictionary __objects
    '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''instance method - public
        returns the dictionary __objects.
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        sets in __objects the obj with key <obj class name>.id.
        '''
        obj_key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[obj_key] = obj

    def save(self):
        '''save - write to file
        serializes __objects to the JSON file
        path: __file_path i.e. evaluates to file.json
        '''
        save_dict = {}
        for key, val in FileStorage.__objects.items():
            save_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(save_dict, f)

    def reload(self):
        '''deserializes the JSON file to __objects.
        if exist: file.json
        '''
        try:
            with open(FileStorage.__file_path, mode='r',
                      encoding='utf-8') as f:
                file_objects = json.load(f)

            for key, val in file_objects.items():
                cls_name = val['__class__']
                del val['__class__']
                self.new(eval(cls_name)(**val))
        except FileNotFoundError:
            pass
