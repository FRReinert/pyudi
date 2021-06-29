from typing import Generator
from pyudi.udi.base import IBaseUDI, Code
from pyudi.fields import gs1
from re import match


class GS1Pattern(IBaseUDI):
    '''UDI Class for GS1 Pattern'''

    encoded_udi_string = ''
    human_readable_udi_string = ''

    def __init__(self, database_field: str):
        self.decode_udi(database_field)

    def decode_udi(self, database_field: str) -> None:
        '''Decode data from barcode string to py'''
        for field, value in self.field_lookup(database_field):
            self.parse_field_to_attribute(field, value)

    def field_lookup(self, database_field: str) -> Generator:
        '''Look for fields within UDI code'''

        # TODO: Make it loops <database_field> instead of <field_list>
        encoded_str = database_field
        for field in self.field_list(gs1):

            re_result = match(field.regex(), encoded_str)
            if re_result:

                # Remove the found string from barcode
                encoded_str = encoded_str.split(re_result[1])[1]
                yield field, re_result[1]

    def parse_field_to_attribute(self, field, field_value):
        '''Add the found field to the instance'''
        setattr(self, field.name, field(field_value))

    def encode_udi(self, to_code: Code = 1) -> str:
        '''Decode obj to UDI_CODE/HUMAN_CODE string. Default is UDI_CODE'''

        for _ in self.get_fields():

            if to_code == 1:
                pass

            elif to_code == 2:
                pass
