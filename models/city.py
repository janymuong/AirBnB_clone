#!/usr/bin/python3
'''module: city
City class module - subclasses BaseModel
'''

from models.base_model import BaseModel


class City(BaseModel):
    '''City class

    attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    '''
    state_id = ''
    name = ''
