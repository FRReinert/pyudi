'''Field Factory'''

from abc import ABC, abstractclassmethod
from pyudi.udi.base import Agency

__all__ = ['FieldFactoryGs1']


class IField(ABC):
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
