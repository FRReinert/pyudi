from abc import ABC, abstractmethod
from typing import Generator
from pyudi.common import Label


class IParser(ABC):
    '''UDI Parser Interface'''

    @abstractmethod
    def parse_from_barcode(self, label: Label, database_str: str, available_fields: list) -> Generator:
        '''Pase from UDI code from barcode'''
        pass

    @abstractmethod
    def parse_from_parameters(self, **kwargs) -> Generator:
        '''Parse UDI from function parameters'''
        pass

    @abstractmethod
    def serialize(self, label: Label, human_readable: bool) -> str:
        '''Serialize a UDI instance to exportable format'''
        pass
