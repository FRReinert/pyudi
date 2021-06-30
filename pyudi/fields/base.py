'''
    This file contain the IField to Interface any agency fields.
    - Do not make attr, properties or methos for IField which only benefits a single agency
    - IField must be enough abstract to implement all possible agencies
'''

from abc import ABC, abstractclassmethod, abstractproperty
from typing import Generator, Tuple


class IFieldFactory(ABC):
    '''Factory Interface to crete Fields'''

    @property
    @abstractproperty
    def __FIELDS() -> Tuple:
        '''Contain a list of all agency field classes'''
        pass

    @classmethod
    def create_field(cls, database_field: str) -> Generator:
        '''Create fields on the fly'''
        pass


class IField(ABC):
    '''Field Interface'''

    data_delimiter: str
    data_size: int
    agency: str
    value: str
    name: str

    @classmethod
    @abstractclassmethod
    def regex(self):
        '''Regex Interface implementation'''
        pass

    def __str__(self):
        return self.value
