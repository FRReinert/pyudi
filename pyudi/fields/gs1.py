'''GS1 fields implementation'''

from typing import Generator

from pyudi.common import Agency, Identifiers, Label, GS1_GS
from pyudi.fields.base import Field, IField, IFieldset, IParser
from pyudi.validators import *

__all__ = ['SSCCField', 'GTINField', 'ContentField', 'BatchLotField', 'ProductionDateField', 'ExpiringDateField',
           'PackingDateField', 'MinimalExpiringField', 'SellExpiringField', 'MaxExpiringDateField',
           'InternalProductVariantField', 'SerialNumberField', 'ConsumerProductVariantField', 'GS1Fieldset']

'''
    Generic GS1 Fields
'''


class GS1AlphanumericField(IField, Field):
    '''Base GS1 Alphanumeric Field'''

    def __init__(self, value: str = None) -> None:
        self.agency = Agency.GS1
        self.value = value
        self.validators = [AllowedCharactersValidator, SizeOverflowValidator, RegexValidator]

    @classmethod
    def regex(cls):
        return r'^%s([\x21-\x22\x25-\x2F\x30-\x39\x3A-\x3F\x41-\x5A\x5F\x61-\x7A]{0,%s})' % (cls.data_delimiter, cls.data_size)


class GS1DateField(IField, Field):
    '''GS1 Date Field'''

    def __init__(self, value: int = None) -> None:
        self.agency = Agency.GS1
        self.value = value
        self.validators = [AllowedCharactersValidator, SizeOverflowValidator, FixedSizeValidator, DateValidator, RegexValidator]

    @classmethod
    def regex(cls):
        return r'^%s(\d{%s})' % (cls.data_delimiter, cls.data_size)


class GS1NumericField(IField, Field):
    '''GS1 Numeric Field'''

    def __init__(self, value: int = None) -> None:
        self.agency = Agency.GS1
        self.value = value
        self.validators = [AllowedCharactersValidator, SizeOverflowValidator, FixedSizeValidator, RegexValidator]

    @classmethod
    def regex(cls):
        return r'^%s(\d{%s})' % (cls.data_delimiter, cls.data_size)


'''
    GS1 Fields
'''


class SSCCField(GS1NumericField):
    '''00 Serial Shipping Container Code (SSCC)'''

    name = Identifiers.SSCC
    data_delimiter = '00'
    data_size = 18
    fixed_size = True


class GTINField(GS1NumericField):
    '''01 Global Trade Item Number (GTIN)'''

    name = Identifiers.GTIN
    data_delimiter = '01'
    data_size = 14
    fixed_size = True


class ContentField(GS1NumericField):
    '''02 Global Trade Item Number (GTIN) of contained trade items'''

    name = Identifiers.CONTENT
    data_delimiter = '02'
    data_size = 14
    fixed_size = True


class BatchLotField(GS1AlphanumericField):
    '''10 Batch or lot number'''

    name = Identifiers.BATCH_LOT
    data_delimiter = '10'
    data_size = 20
    fixed_size = False


class ProductionDateField(GS1DateField):
    '''11 Production date (YYMMDD)'''

    name = Identifiers.PROD_DATE
    data_delimiter = '11'
    data_size = 6
    fixed_size = True


class ExpiringDateField(GS1DateField):
    '''12 Due date (YYMMDD)'''

    name = Identifiers.DUE_DATE
    data_delimiter = '12'
    data_size = 6
    fixed_size = True


class PackingDateField(GS1DateField):
    '''13 Packaging date (YYMMDD)'''

    name = Identifiers.PACK_DATE
    data_delimiter = '13'
    data_size = 6
    fixed_size = True


class MinimalExpiringField(GS1DateField):
    '''15 Best before date (YYMMDD)'''

    name = Identifiers.BEST_BEFORE_OR_BEST_BY
    data_delimiter = '15'
    data_size = 6
    fixed_size = True


class SellExpiringField(GS1DateField):
    '''16 Sell by date (YYMMDD)'''

    name = Identifiers.SELL_BY
    data_delimiter = '16'
    data_size = 6
    fixed_size = True


class MaxExpiringDateField(GS1DateField):
    '''17 Expiration date (YYMMDD)'''

    name = Identifiers.USE_BY_OR_EXPIRY
    data_delimiter = '17'
    data_size = 6
    fixed_size = True


class InternalProductVariantField(GS1NumericField):
    '''20 Internal product variant'''

    name = Identifiers.VARIANT
    data_delimiter = '20'
    data_size = 2
    fixed_size = True


class SerialNumberField(GS1AlphanumericField):
    '''21 Serial number'''

    name = Identifiers.SERIAL
    data_delimiter = '21'
    data_size = 20
    fixed_size = False


class ConsumerProductVariantField(GS1AlphanumericField):
    '''21 Serial number'''

    name = Identifiers.CPV
    data_delimiter = '22'
    data_size = 20
    fixed_size = False
