#!/usr/bin/python3
'''module: state
State class module - subclasses BaseModel
'''

from models.base_model import BaseModel


class State(BaseModel):
    '''State class

    attributes:
        name: string - empty string
    '''
    name = ''
