from abc import ABC, abstractmethod
from pyudi.common import Label
from pyudi.fields.base import IField


class ISerializer(ABC):

    @abstractmethod
    def serialize_to_human_readable_str(self) -> str:
        '''Transform fields in UDI code'''
        pass

    @abstractmethod
    def serialize_to_barcode_str(self, label: Label, fixed_fields: list[IField], variable_fields: list[IField]) -> str:
        '''Transform fields in UDI code'''
        pass
