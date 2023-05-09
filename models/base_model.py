#!/usr/bin/python3
'''module: base_model
Base (class) model for:
subclassing/inheritance, serialization and deserilaization is the superclass.
'''

from datetime import datetime
import uuid


class BaseModel:
    '''Defines all common attributes/methods for other classes
    '''
    def __init__(self):
        '''constructor method
        Initialize BaseModel instance attributes

        attributes:
            id: (string) universally unique identifier
            created_at: (datetime) timestamp of time of creation
            updated_at: (datetime) timestamp
        '''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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
