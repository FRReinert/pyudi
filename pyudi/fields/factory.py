'''Field Factory'''

from pyudi.fields.base import IFieldFactory
from pyudi.fields.gs1 import *
from pyudi.exceptions import DeserializingException
from typing import Generator
from re import match

__all__ = ['FieldFactoryGs1']


class FieldFactoryGs1(IFieldFactory):
    '''Field Factory'''

    __FIELDS = [
        SSCCField, GTINField, ContentField, BatchLotField, ProductionDateField, ExpiringDateField,
        PackingDateField, MinimalExpiringField, SellExpiringField, MaxExpiringDateField,
        InternalProductVariantField, SerialNumberField, ConsumerProductVariantField
    ]

    @classmethod
    def create_fields(cls, database_field: str) -> Generator:
        '''Decode data from barcode string to py'''

        encoded_str = database_field  # Copy parameter
        is_encoded_str_valid = True  # Flow Control. Break loop if field not found

        while is_encoded_str_valid:

            is_encoded_str_valid = False
            for field in cls.__FIELDS:

                re_result = match(field.regex(), encoded_str)
                if re_result:

                    # Remove found string from database_field
                    encoded_str = encoded_str.split(re_result[0])[1]
                    is_encoded_str_valid = True

                    yield field, re_result[1]
                    break
