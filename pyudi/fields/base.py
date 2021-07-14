'''Field Factory'''

from abc import ABC, abstractclassmethod
from pyudi.common import Agency
from pyudi.validators import IValidator


class IField(ABC):
    '''Field Interface'''

    data_delimiter: str
    fixed_size: bool
    data_size: int
    agency: Agency
    value: str
    name: str

    @classmethod
    @abstractclassmethod
    def regex(self):
        '''Regex Interface implementation'''
        pass


class Field:

    validators: list[IValidator]

    def __str__(self):
        return self.value

    def validate(self, *args, **kwargs):
        for validator in self.validators:
            validator.validate()
