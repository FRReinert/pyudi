'''Field Factory'''

from abc import ABCMeta, abstractclassmethod, abstractmethod, abstractproperty
from typing import Generator
from pyudi.common import Agency

__all__ = ['FieldFactoryGs1']


class IField(metaclass=ABCMeta):
    '''Field Interface'''

    data_delimiter: str
    data_size: int
    agency: Agency
    value: str
    name: str

    @classmethod
    @abstractclassmethod
    def regex(self):
        '''Regex Interface implementation'''
        pass

    def __str__(self):
        return self.value


class IFieldset(metaclass=ABCMeta):
    '''Interface Fieldset to wrap all fields'''

    @property
    @abstractproperty
    def __fieldset__(self) -> list[str]:
        '''Contain all field names'''
        pass

    @abstractmethod
    def parse(self, database_str: str) -> None:
        '''From UDI code to instance fields'''
        pass

    @abstractmethod
    def serialize(self) -> str:
        '''Instance fields  to UDI code'''

    def get_fields(self, show_empty=False) -> Generator:
        '''Retrieve fields from instance fieldset'''
        
        if show_empty:
            
            for field in self.__fieldset__:
                yield getattr(self, field)
        
        else:
            
            for field in self.__fieldset__:
                if field.value:
                    yield getattr(self, field)

