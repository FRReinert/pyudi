'''
This file contains the GS1 fields declaration

    TODO:
    - Verify with GS1 what is the sequence of fields to be evaluated and ask for a oficial document to be referenced here
    - Without a proper sequence a field can be matched at any point of the code
    - Example sequence: 00xxxx01xxxx10xxx11xxx17xxx(...)
'''

from pyudi.fields.base import GS1AlphanumericField, GS1DateField, GS1NumericField


class SSCCField(GS1NumericField):
    '''00 Serial Shipping Container Code (SSCC)'''

    name = 'FIELD__SSCC'
    data_delimiter = '00'
    data_size = 18


class GTINField(GS1NumericField):
    '''01 Global Trade Item Number (GTIN)'''

    name = 'FIELD__GTIN'
    data_delimiter = '01'
    data_size = 14


class ContentField(GS1NumericField):
    '''02 Global Trade Item Number (GTIN) of contained trade items'''

    name = 'FIELD__CONTENT'
    data_delimiter = '02'
    data_size = 14


class BatchLotField(GS1AlphanumericField):
    '''10 Batch or lot number'''

    name = 'FIELD__BATCH_LOT'
    data_delimiter = '10'
    data_size = 20


class ProductionDateField(GS1DateField):
    '''11 Production date (YYMMDD)'''

    name = 'FIELD__PROD_DATE'
    data_delimiter = '11'
    data_size = 6


class ExpiringDateField(GS1DateField):
    '''12 Due date (YYMMDD)'''

    name = 'FIELD__DUE_DATE'
    data_delimiter = '12'
    data_size = 6


class PackingDateField(GS1DateField):
    '''13 Packaging date (YYMMDD)'''

    name = 'FIELD__PACK_DATE'
    data_delimiter = '13'
    data_size = 6


class MinimalExpiringField(GS1DateField):
    '''15 Best before date (YYMMDD)'''

    name = 'FIELD__BEST_BEFORE_OR_BEST_BY'
    data_delimiter = '15'
    data_size = 6


class SellExpiringField(GS1DateField):
    '''16 Sell by date (YYMMDD)'''

    name = 'FIELD__SELL_BY'
    data_delimiter = '16'
    data_size = 6


class MaxExpiringDateField(GS1DateField):
    '''17 Expiration date (YYMMDD)'''

    name = 'FIELD__USE_BY_OR_EXPIRY'
    data_delimiter = '17'
    data_size = 6


class InternalProductVariantField(GS1NumericField):
    '''20 Internal product variant'''

    name = 'FIELD__VARIANT'
    data_delimiter = '20'
    data_size = 2


class SerialNumberField(GS1AlphanumericField):
    '''21 Serial number'''

    name = 'FIELD__SERIAL'
    data_delimiter = '21'
    data_size = 20


class ConsumerProductVariantField(GS1AlphanumericField):
    '''21 Serial number'''

    name = 'FIELD__CPV'
    data_delimiter = '22'
    data_size = 20

__fields = (
    SSCCField, GTINField, ContentField, BatchLotField, ProductionDateField, ExpiringDateField, 
    PackingDateField, MinimalExpiringField, SellExpiringField, MaxExpiringDateField, 
    InternalProductVariantField, SerialNumberField, ConsumerProductVariantField
)