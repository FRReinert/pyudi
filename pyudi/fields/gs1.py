'''GS1 fields implementation'''

from pyudi.udi.base import IStructureUDI
import re

from pyudi.common import Agency, Delimiter, Identifiers
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


class GTINField(GS1NumericField):
    '''01 Global Trade Item Number (GTIN)'''

    name = Identifiers.GTIN
    data_delimiter = '01'
    data_size = 14


class ContentField(GS1NumericField):
    '''02 Global Trade Item Number (GTIN) of contained trade items'''

    name = Identifiers.CONTENT
    data_delimiter = '02'
    data_size = 14


class BatchLotField(GS1AlphanumericField):
    '''10 Batch or lot number'''

    name = Identifiers.BATCH_LOT
    data_delimiter = '10'
    data_size = 20


class ProductionDateField(GS1DateField):
    '''11 Production date (YYMMDD)'''

    name = Identifiers.PROD_DATE
    data_delimiter = '11'
    data_size = 6


class ExpiringDateField(GS1DateField):
    '''12 Due date (YYMMDD)'''

    name = Identifiers.DUE_DATE
    data_delimiter = '12'
    data_size = 6


class PackingDateField(GS1DateField):
    '''13 Packaging date (YYMMDD)'''

    name = Identifiers.PACK_DATE
    data_delimiter = '13'
    data_size = 6


class MinimalExpiringField(GS1DateField):
    '''15 Best before date (YYMMDD)'''

    name = Identifiers.BEST_BEFORE_OR_BEST_BY
    data_delimiter = '15'
    data_size = 6


class SellExpiringField(GS1DateField):
    '''16 Sell by date (YYMMDD)'''

    name = Identifiers.SELL_BY
    data_delimiter = '16'
    data_size = 6


class MaxExpiringDateField(GS1DateField):
    '''17 Expiration date (YYMMDD)'''

    name = Identifiers.USE_BY_OR_EXPIRY
    data_delimiter = '17'
    data_size = 6


class InternalProductVariantField(GS1NumericField):
    '''20 Internal product variant'''

    name = Identifiers.VARIANT
    data_delimiter = '20'
    data_size = 2


class SerialNumberField(GS1AlphanumericField):
    '''21 Serial number'''

    name = Identifiers.SERIAL
    data_delimiter = '21'
    data_size = 20


class ConsumerProductVariantField(GS1AlphanumericField):
    '''21 Serial number'''

    name = Identifiers.CPV
    data_delimiter = '22'
    data_size = 20


class Gs1Parser(IParser):
    '''Parses and serializes GS1 Fields'''

    def __init__(self, fieldset_object: IFieldset, delimiter: Delimiter):
        self.fieldset_object = fieldset_object
        self.delimiter = delimiter

    def _parse_from_udi(self, database_str: str) -> None:
        '''Parse from UDI code'''

        # FNC1 Delimiter
        if self.delimiter == Delimiter.FNC1_GS:
            for chunk_str in database_str.split('\x1d'):
                
                for identifier_name, identifier_class in self.fieldset_object.fields.items():
                    result = re.match(identifier_class.regex(), chunk_str)
                    
                    if result:
                        setattr(self.fieldset_object, identifier_name, identifier_class(result[0]))
                        break  # break the second loop. move to next <chunk_str>
        
        # Field Size delimitation
        else:
            pass

    def _parse_from_parameters(self, **kwargs) -> None:
        '''Parse from kwarg parameters'''
        supplied_parameters = kwargs.keys()
        for identifier_name, identifier_class in self.fieldset_object.fields.items():
            if identifier_name in supplied_parameters:
                setattr(self.fieldset_object, identifier_name, identifier_class(kwargs[identifier_name]))


    def parse(self, database_str: str = None, **kwargs) -> None:
        '''Waiting for more information from GS1 on how to parse'''
        if database_str:
            self._parse_from_udi(database_str)
        else:
            self._parse_from_parameters(**kwargs)


    def serialize(self, human_readable=False) -> str:
        '''Transform fields in UDI code'''

        udi = ''

        if human_readable:
            for field in self.get_fields(show_empty=False):
                udi += '(' + field.data_delimeter + ')' + field.value

        else:
            for field in self.get_fields(show_empty=False):
                udi += '\x1d' + field.data_delimiter + field.value

        return udi


class GS1Fieldset(IFieldset):
    '''Represent a container with GS1 Fields'''

    def __init__(self, parent_structure:IStructureUDI, delimiter: Delimiter, *args, **kwargs):

        # Pointer to parent UDI Structure (not needed yet)
        self.parent_structure = parent_structure

        # Identifier Class for GS1
        self.fields = {
            'SSCC':SSCCField, 'GTIN':GTINField, 'CONTENT':ContentField, 'BATCH_LOT':BatchLotField, 
            'PROD_DATE':ProductionDateField, 'DUE_DATE':ExpiringDateField, 'PACK_DATE':PackingDateField,
            'BEST_BEFORE_OR_BEST_BY':MinimalExpiringField, 'SELL_BY':SellExpiringField, 'USE_BY_OR_EXPIRY':MaxExpiringDateField,
            'VARIANT':InternalProductVariantField, 'SERIAL':SerialNumberField, 'CPV':ConsumerProductVariantField
        }

        # Initialize Fields
        self.initialize_fields()

        # Parse user parameters to fields
        self.parser = Gs1Parser(self, delimiter=delimiter)
        self.parser.parse(*args, **kwargs)
