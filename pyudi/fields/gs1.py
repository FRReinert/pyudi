'''GS1 fields implementation'''

from dataclasses import dataclass
from pyudi.common import Agency
from pyudi.fields.base import IField, IFieldset
from typing import Optional


__all__ = ['SSCCField', 'GTINField', 'ContentField', 'BatchLotField', 'ProductionDateField', 'ExpiringDateField',
           'PackingDateField', 'MinimalExpiringField', 'SellExpiringField', 'MaxExpiringDateField',
           'InternalProductVariantField', 'SerialNumberField', 'ConsumerProductVariantField']


'''
    Generic GS1 Fields
'''


class GS1AlphanumericField(IField):
    '''Base GS1 Alphanumeric Field'''

    def __init__(self, agency: Agency, value: str) -> None:
        self.agency = agency
        self.value = value

    @classmethod
    def regex(cls):
        '''
        TODO: 
            - flexible amount of chars will only work if there is any special delimiter character (Which it doesnt have)
            - This regex is specified at GS1 website
        '''
        return r'^%s([\x21-\x22\x25-\x2F\x30-\x39\x3A-\x3F\x41-\x5A\x5F\x61-\x7A]{0,%s})' % (cls.data_delimiter, cls.data_size)


class GS1DateField(IField):
    '''GS1 Date Field'''

    def __init__(self, agency: Agency, value: int) -> None:
        self.agency = agency
        self.value = value

    @classmethod
    def regex(cls):
        return r'^%s(\d{%s})' % (cls.data_delimiter, cls.data_size)


class GS1NumericField(IField):
    '''GS1 Numeric Field'''

    def __init__(self, agency: Agency, value: int) -> None:
        self.agency = agency
        self.value = value

    @classmethod
    def regex(cls):
        return r'^%s(\d{%s})' % (cls.data_delimiter, cls.data_size)


'''
    GS1 Fields
'''


class SSCCField(GS1NumericField):
    '''00 Serial Shipping Container Code (SSCC)'''

    agency: Agency = Agency.GS1
    name = 'SSCC'
    data_delimiter = '00'
    data_size = 18


class GTINField(GS1NumericField):
    '''01 Global Trade Item Number (GTIN)'''

    agency: Agency = Agency.GS1
    name = 'GTIN'
    data_delimiter = '01'
    data_size = 14


class ContentField(GS1NumericField):
    '''02 Global Trade Item Number (GTIN) of contained trade items'''

    agency: Agency = Agency.GS1
    name = 'CONTENT'
    data_delimiter = '02'
    data_size = 14


class BatchLotField(GS1AlphanumericField):
    '''10 Batch or lot number'''

    agency: Agency = Agency.GS1
    name = 'BATCH_LOT'
    data_delimiter = '10'
    data_size = 20


class ProductionDateField(GS1DateField):
    '''11 Production date (YYMMDD)'''

    agency: Agency = Agency.GS1
    name = 'PROD_DATE'
    data_delimiter = '11'
    data_size = 6


class ExpiringDateField(GS1DateField):
    '''12 Due date (YYMMDD)'''

    agency: Agency = Agency.GS1
    name = 'DUE_DATE'
    data_delimiter = '12'
    data_size = 6


class PackingDateField(GS1DateField):
    '''13 Packaging date (YYMMDD)'''

    agency: Agency = Agency.GS1
    name = 'PACK_DATE'
    data_delimiter = '13'
    data_size = 6


class MinimalExpiringField(GS1DateField):
    '''15 Best before date (YYMMDD)'''

    agency: Agency = Agency.GS1
    name = 'BEST_BEFORE_OR_BEST_BY'
    data_delimiter = '15'
    data_size = 6


class SellExpiringField(GS1DateField):
    '''16 Sell by date (YYMMDD)'''

    agency: Agency = Agency.GS1
    name = 'SELL_BY'
    data_delimiter = '16'
    data_size = 6


class MaxExpiringDateField(GS1DateField):
    '''17 Expiration date (YYMMDD)'''

    agency: Agency = Agency.GS1
    name = 'USE_BY_OR_EXPIRY'
    data_delimiter = '17'
    data_size = 6


class InternalProductVariantField(GS1NumericField):
    '''20 Internal product variant'''

    agency: Agency = Agency.GS1
    name = 'VARIANT'
    data_delimiter = '20'
    data_size = 2


class SerialNumberField(GS1AlphanumericField):
    '''21 Serial number'''

    agency: Agency = Agency.GS1
    name = 'SERIAL'
    data_delimiter = '21'
    data_size = 20


class ConsumerProductVariantField(GS1AlphanumericField):
    '''21 Serial number'''

    agency: Agency = Agency.GS1
    name = 'CPV'
    data_delimiter = '22'
    data_size = 20


@dataclass
class GS1Fieldset(IFieldset):
    '''Represent a container with GS1 Fields'''

    SSCCField: Optional[SSCCField]
    GTINField: Optional[GTINField]
    ContentField: Optional[ContentField]
    BatchLotField: Optional[BatchLotField]
    ProductionDateField: Optional[ProductionDateField]
    ExpiringDateField: Optional[ExpiringDateField]
    PackingDateField: Optional[PackingDateField]
    MinimalExpiringField: Optional[MinimalExpiringField]
    SellExpiringField: Optional[SellExpiringField]
    MaxExpiringDateField: Optional[MaxExpiringDateField]
    InternalProductVariantField: Optional[InternalProductVariantField]
    SerialNumberField: Optional[SerialNumberField]
    ConsumerProductVariantField: Optional[ConsumerProductVariantField]

    def parse(self, database_str: str) -> None:
        return super().parse(database_str)

    def serialize(self) -> str:
        return super().serialize()