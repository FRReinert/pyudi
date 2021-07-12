'''Field Factory'''

from abc import ABC, abstractclassmethod, abstractmethod
from typing import Generator
from pyudi.common import Agency


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


class IParser(ABC):
    '''UDI Parser Interface'''

    @abstractmethod
    def parse(self, database_str: str = None, **kwargs) -> None:
        '''Pase from UDI code or parameters to instance fields'''
        pass

    @abstractmethod
    def serialize(self) -> str:
        '''Instance fields  to UDI code'''
        pass


class IFieldset(ABC):
    '''Field container Interface'''

    def initialize_fields(self) -> None:
        '''Initialize all UDI fields with None'''
        for field_name in self.fields.keys():
            setattr(self, field_name, None)
    
    def get_fields(self, show_empty=False) -> Generator:
        '''Return all field objects'''
        fields = [getattr(self, field_name) for field_name in self.fields.keys()]

        if show_empty:
            gen = (field for field in fields)  # yield every field
        else:
            # yield only if field IS NOT None
            gen = (field for field in fields if field.value)

        return gen
