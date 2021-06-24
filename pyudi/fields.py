from abc import ABCMeta, abstractproperty

__all__ = [
    'GTINField', 'ContentField', 'BatchLotField', 'ProductionDateField', 'ExpiringDateField', 
    'PackingDateField', 'MinimalExpiringField', 'SellExpiringField', 'MaxExpiringDateField', 
    'MaxExpiringDateField', 'SerialNumberField', 'ConsumerProductVariantField'
]


class IField(metaclass=ABCMeta):
    '''Base data types for GS1 labels'''

    data_delimiter: str
    data_size: int
    agency: str
    name: str

    @abstractproperty
    def re(self):
        '''Return a valid Regular Expression'''


class AlphanumericField(IField):
    '''Base Alphanumeric Field'''

    @property
    def re(self):
        return fr'^{self.data_delimiter}([\x21-\x22\x25-\x2F\x30-\x39\x3A-\x3F\x41-\x5A\x5F\x61-\x7A]{0,{self.data_size}})$'


class DateField(IField):
    '''Base Date Field'''

    # TODO: Verify other Patterns beyond GS1. 
    # - Verify if all of them use 6 digits
    # - Verify if all of them use the same date format
    data_size = 6

    @property
    def re(self):
        return fr'^{self.data_delimiter}(\d{self.data_size})$'


class NumericField(IField):
    '''Base Numeric Field'''

    @property
    def re(self):
        return fr'^{self.data_delimiter}(\d{{self.data_size}})$'


class SSCCField(NumericField):
    '''00 Serial Shipping Container Code (SSCC)'''

    agency = 'GS1'
    name = 'SSCC'
    data_delimiter = '00'
    data_size = 18


class GTINField(NumericField):
    '''01 Global Trade Item Number (GTIN)'''

    agency = 'GS1'
    name = 'GTIN'
    data_delimiter = '01'
    data_size = 14


class ContentField(NumericField):
    '''02 Global Trade Item Number (GTIN) of contained trade items'''

    content = 'CONTENT'
    data_delimiter = '02'
    data_size = 14


class BatchLotField(AlphanumericField):
    '''10 Batch or lot number'''

    agency = 'GS1'
    name = 'BATCH/LOT'
    data_delimiter = '10'
    data_size = 20


class ProductionDateField(DateField):
    '''11 Production date (YYMMDD)'''

    agency = 'GS1'
    name = 'PROD DATE'
    data_delimiter = '11'


class ExpiringDateField(DateField):
    '''12 Due date (YYMMDD)'''

    agency = 'GS1'
    name = 'DUE DATE'
    data_delimiter = '12'


class PackingDateField(DateField):
    '''13 Packaging date (YYMMDD)'''

    agency = 'GS1'
    name = 'PACK DATE'
    data_delimiter = '13'


class MinimalExpiringField(DateField):
    '''15 Best before date (YYMMDD)'''

    agency = 'GS1'
    name = 'BEST BEFORE or BEST BY'
    data_delimiter = '15'


class SellExpiringField(DateField):
    '''16 Sell by date (YYMMDD)'''

    agency = 'GS1'
    name = 'SELL BY'
    data_delimiter = '16'


class MaxExpiringDateField(DateField):
    '''17 Expiration date (YYMMDD)'''

    agency = 'GS1'
    name = 'USE BY OR EXPIRY'
    data_delimiter = '17'


class MaxExpiringDateField(NumericField):
    '''20 Internal product variant'''

    agency = 'GS1'
    name = 'VARIANT'
    data_delimiter = '20'
    data_size = 2


class SerialNumberField(AlphanumericField):
    '''21 Serial number'''

    agency = 'GS1'
    name = 'SERIAL'
    data_delimiter = '21'
    data_size = 20


class ConsumerProductVariantField(AlphanumericField):
    '''21 Serial number'''

    agency = 'GS1'
    name = 'CPV'
    data_delimiter = '22'
    data_size = 20