from abc import ABC
from typing import Iterable
from pyudi.fields.base import IField


class IFieldset(ABC):
    '''Field container Interface'''
    pass


class Fieldset:
    '''Field container basic behaviors'''

    def initialize_fields(self) -> None:
        '''Initialize all UDI fields without value'''
        for field_name, field_class in self.fields.items():
            setattr(self, field_name, field_class())

    def get_fixed_size_fields(self, show_empty_fields: bool = False) -> Iterable[IField]:
        '''Return fixed size fields'''

        # Filter Fixed/Variable size fields
        filtered_field_names = filter(lambda field_name: getattr(self, field_name).fixed_size == True, self.fields.keys())

        # Filter empty fields
        if show_empty_fields == False:
            filtered_field_names = filter(lambda field_name: True if getattr(self, field_name).value else False, filtered_field_names)

        # Apply filter
        return (getattr(self, field) for field in filtered_field_names)

    def get_variable_size_fields(self, show_empty_fields: bool=False) -> Iterable[IField]:
        '''Return variable size fields'''

        # Filter Fixed/Variable size fields
        filtered_field_names = filter(lambda field_name: getattr(self, field_name).fixed_size == False, self.fields.keys())

        # Filter empty/used fields
        if show_empty_fields == False:
            filtered_field_names = filter(lambda field_name: True if getattr(self, field_name).value else False, filtered_field_names)

        # Apply filter
        return (getattr(self, field) for field in filtered_field_names)

    def get_fields(self, show_empty_fields=False) -> Iterable[IField]:
        '''Return all field objects'''
        
        fields = (getattr(self, field_name) for field_name in self.fields.keys())

        if show_empty_fields == False:
            fields = filter(lambda field: hasattr(field, 'value'), fields)

        return fields
