#!/usr/bin/python3
'''module: user
User class module - subclasses BaseModel
'''

from models.base_model import BaseModel


class User(BaseModel):
    '''User class

    attributes:
        email: - empty string
        password: - empty string
        first_name: - empty string
        last_name: - empty string
    '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
