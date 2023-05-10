#!/usr/bin/python3
'''module: base_model
Base (class) model for:
subclassing/inheritance, serialization and deserilaization is the superclass.
'''

import uuid
from datetime import datetime

import models


class BaseModel:
    '''Defines all common attributes/methods for other classes
    '''
    def __init__(self, *args, **kwargs):
        '''constructor method
        Initialize BaseModel instance attributes

        args:
            are arbitrary variable args and arbitrary named args:
            *args: a Tuple that contains all arguments to construtor
            **kwargs: a dictionary key-worded(key/value) arguments

        attributes:
            id: (string) universally unique identifier
            created_at: (datetime) timestamp of time of creation
            updated_at: (datetime) timestamp
        '''

        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, val)
        # if kwargs:
        #     for key, val in kwargs.items():
        #         if key not in ('__class__', 'created_at', 'updated_at'):
        #             setattr(self, key, val)
        #         elif key in ('created_at', 'updated_at'):
        #             setattr(self, key,
        #                     datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
        #                     )
        #     self.id = kwargs.get('id', str(uuid.uuid4()))
        #     self.created_at = kwargs.get('created_at', datetime.now())
        #     self.updated_at = kwargs.get('updated_at', datetime.now())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''__str__
        return string representation of the BaseModel instance
        '''
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        '''update method
        overwrite value of public instance attribute 'updated_at'
        with the current datetime
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''__dict__:
        return ISO dictionary representation of the BaseModel instance
        contains all keys/values of __dict__ of the instance
        '''

        dict_repr = self.__dict__.copy()

        dict_repr['__class__'] = type(self).__name__
        dict_repr['created_at'] = dict_repr['created_at'].isoformat()
        dict_repr['updated_at'] = dict_repr['updated_at'].isoformat()

        return dict_repr
