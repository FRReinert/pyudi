'''Field Factory'''

from abc import ABCMeta, abstractclassmethod, abstractmethod
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

    @abstractmethod
    def parse(self, database_str: str) -> None:
        '''From UDI code to instance fields'''
        pass

    @abstractmethod
    def serialize(self) -> str:
        '''Instance fields  to UDI code'''
