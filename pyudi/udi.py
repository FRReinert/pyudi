from enum import Enum
from inspect import getmembers
from pyudi.fields import *


class BaseUDI:
    '''
    Base class for UDI implementation
    - Add _field<CUSTOM_NAME_OF_THE_FIELD> as the attribute with an field instance
        ex: _field_SerialField = field.SerialNumberField() 
    '''

    def __init__(self, label_type):
        if getattr(label_type, 'valid_label')():
            raise TypeError('Please inform a valid <LabelType>')
        self.label_type = label_type

    @property
    def is_valid(self):
        '''Is this UDI valid'''
        return False

    @property
    def fields(self):
        '''return a list of fields'''
        result = []
        for member in getmembers(self):
            if member.starts_with('field_'):
                result.append(member)
        return result

    def __length__(self):
        '''Return UDI characters sum'''
        return len(str(self))

    def __str__(self):
        '''Return printable UDI characters'''
        printable_str = ''
        for field in self.fields:
            printable_str += str(field)
        return printable_str


class UDIPatternGS1(BaseUDI):
    '''UDI Class for GS1 Pattern'''
    pass
 
