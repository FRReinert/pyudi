from abc import ABC, abstractmethod
from typing import Iterator
from pyudi.common import Label


class IParser(ABC):
    '''UDI Parser Interface'''

    @abstractmethod
    def parse_from_barcode(self, label: Label, database_str: str, available_fields: list) -> Iterator:
        '''Pase from UDI code from barcode'''
        pass

    @abstractmethod
    def parse_from_parameters(self, **kwargs) -> Iterator:
        '''Parse UDI from function parameters'''
        pass

    @abstractmethod
    def serialize_to_human_readable_str(self) -> str:
        '''Serialize a UDI instance to human readable format'''
        pass

    @abstractmethod
    def serialize_to_barcode_str(self, label: Label) -> str:
        '''Serialize a UDI instance to barcode format'''
        pass
