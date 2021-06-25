from typing import Any, Generator, List
from inspect import getmembers
from abc import ABCMeta, abstractmethod, abstractproperty

class IBaseUDI(metaclass=ABCMeta):
    '''
    Base class for UDI implementation
    - Add _field<CUSTOM_NAME_OF_THE_FIELD> as the attribute with an field instance
        ex: _field_SerialField = field.SerialNumberField() 
    '''

    @abstractmethod
    def __init__(self):
        '''Interface Validate Field'''

    @property
    @abstractproperty
    def human_readable_udi_string(self) -> str:
        '''Interface attribute for UDI String'''

    @property
    @abstractproperty
    def encoded_udi_string(self) -> str:
        '''Interface attribute for encoded UDI String'''

    @abstractmethod
    def encode_udi(self) -> None:
        '''Interface method to encode UDI from string'''

    @abstractmethod
    def decode_udi(self) -> None:
        '''Interface method to decode UDI from instance'''

    def __length__(self) -> int:
        '''Return UDI characters sum'''
        return len(str(self))

    def __str__(self) -> str:
        '''Return printable UDI characters'''
        printable_str = ''
        for field in self.fields:
            printable_str += str(field)
        return printable_str

    def is_valid(self) -> bool:
        '''Is the UDI valid'''
        return False

    def get_fields(self) -> List:
        '''return a list of fields'''
        result = []
        for member in getmembers(self):
            if member.starts_with('field_'):
                result.append(member)
        return result

    @staticmethod
    def field_list(agency_field_module: Any) -> Generator:
        '''Return a list of field classes for the specific agency'''
        for field_class in getattr(agency_field_module, '__fields'):
            yield field_class
