from abc import ABC
from typing import Generator
from pyudi.fields.base import IField


class IFieldset(ABC):
    '''Field container Interface'''

    def initialize_fields(self) -> None:
        '''Initialize all UDI fields with None'''
        for field_name in self.fields.keys():
            setattr(self, field_name, None)
    

class Fieldset:
    '''Field container basic behaviors'''

    def get_fixed_size_fields(self, show_empty_fields: bool=False) -> Generator[IField]:
        '''Return only fixed size fields'''
        fields = [getattr(self, field_name) for field_name in self.fields.keys()]
        fields = filter(lambda field: field.fixed_size == True, fields)

        if show_empty_fields == False:
            fields = (field for field in fields if field.value)

        return fields

    def get_variable_size_fields(self, show_empty_fields: bool=False) -> Generator[IField]:
        '''Return variable size fields'''
        fields = [getattr(self, field_name) for field_name in self.fields.keys()]
        fields = filter(lambda field: field.fixed_size == False, fields)

        if show_empty_fields == False:
            fields = (field for field in fields if field.value)

        return fields

    def get_fields(self, show_empty_fields=False, fixed_size_only=False) -> Generator[IField]:
        '''Return all field objects'''
        fields = [getattr(self, field_name) for field_name in self.fields.keys()]

        if show_empty_fields == False:
            fields = (field for field in fields if field.value)

        return fields
