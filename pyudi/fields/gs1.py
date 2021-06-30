'''GS1 fields implementation'''

from pyudi.fields.base import IField


__all__ = ['SSCCField', 'GTINField', 'ContentField', 'BatchLotField', 'ProductionDateField', 'ExpiringDateField',
           'PackingDateField', 'MinimalExpiringField', 'SellExpiringField', 'MaxExpiringDateField',
           'InternalProductVariantField', 'SerialNumberField', 'ConsumerProductVariantField']


'''
Base Fields
'''


class GS1AlphanumericField(IField):
    '''Base GS1 Alphanumeric Field'''

    def __init__(self, agency: str, value: str) -> None:
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

    def __init__(self, agency: str, value: int) -> None:
        self.agency = agency
        self.value = value

    @classmethod
    def regex(cls):
        return r'^%s(\d{%s})' % (cls.data_delimiter, cls.data_size)


class GS1NumericField(IField):
    '''GS1 Numeric Field'''

    def __init__(self, agency: str, value: int) -> None:
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

    agency = 'gs1'
    name = 'field_SSCC'
    data_delimiter = '00'
    data_size = 18


class GTINField(GS1NumericField):
    '''01 Global Trade Item Number (GTIN)'''

    agency = 'gs1'
    name = 'field_GTIN'
    data_delimiter = '01'
    data_size = 14


class ContentField(GS1NumericField):
    '''02 Global Trade Item Number (GTIN) of contained trade items'''

    agency = 'gs1'
    name = 'field_CONTENT'
    data_delimiter = '02'
    data_size = 14


class BatchLotField(GS1AlphanumericField):
    '''10 Batch or lot number'''

    agency = 'gs1'
    name = 'field_BATCH_LOT'
    data_delimiter = '10'
    data_size = 20


class ProductionDateField(GS1DateField):
    '''11 Production date (YYMMDD)'''

    agency = 'gs1'
    name = 'field_PROD_DATE'
    data_delimiter = '11'
    data_size = 6


class ExpiringDateField(GS1DateField):
    '''12 Due date (YYMMDD)'''

    agency = 'gs1'
    name = 'field_DUE_DATE'
    data_delimiter = '12'
    data_size = 6


class PackingDateField(GS1DateField):
    '''13 Packaging date (YYMMDD)'''

    agency = 'gs1'
    name = 'field_PACK_DATE'
    data_delimiter = '13'
    data_size = 6


class MinimalExpiringField(GS1DateField):
    '''15 Best before date (YYMMDD)'''

    agency = 'gs1'
    name = 'field_BEST_BEFORE_OR_BEST_BY'
    data_delimiter = '15'
    data_size = 6


class SellExpiringField(GS1DateField):
    '''16 Sell by date (YYMMDD)'''

    agency = 'gs1'
    name = 'field_SELL_BY'
    data_delimiter = '16'
    data_size = 6


class MaxExpiringDateField(GS1DateField):
    '''17 Expiration date (YYMMDD)'''

    agency = 'gs1'
    name = 'field_USE_BY_OR_EXPIRY'
    data_delimiter = '17'
    data_size = 6


class InternalProductVariantField(GS1NumericField):
    '''20 Internal product variant'''

    agency = 'gs1'
    name = 'field_VARIANT'
    data_delimiter = '20'
    data_size = 2


class SerialNumberField(GS1AlphanumericField):
    '''21 Serial number'''

    agency = 'gs1'
    name = 'field_SERIAL'
    data_delimiter = '21'
    data_size = 20


class ConsumerProductVariantField(GS1AlphanumericField):
    '''21 Serial number'''

    agency = 'gs1'
    name = 'field_CPV'
    data_delimiter = '22'
    data_size = 20
