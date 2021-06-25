from pyudi.udi.base import IBaseUDI
from pyudi.fields import gs1
from enum import Enum
from re import match


class Code(Enum):
    '''Used to verify what decode should be used'''

    BAR_CODE = 1
    HUMAN_CODE = 2


class GS1Pattern(IBaseUDI):
    '''UDI Class for GS1 Pattern'''

    encoded_udi_string = ''
    human_readable_udi_string = ''

    def __init__(self, barcode: str):
        self.decode_udi(barcode)

    def decode_udi(self, barcode: str) -> None:
        '''
        Decode data from barcode string to py
            NOT WORKING - SEE MY COMMENTS AT field_list IMPLEMENTATION
        '''
        encoded_str = barcode
        for field in self.field_list(gs1):

            re_result = match(field.regex(), encoded_str)
            if re_result:

                # Add the found field to the instance
                setattr(self, field.name, field(re_result[1]))

                # Remove the found string fron barcode
                encoded_str = encoded_str.split(re_result[1])[1]

    def encode_udi(self, to_code: Code = 1) -> str:
        '''Decode obj to BAR_CODE/HUMAN_CODE string. Default is BAR_CODE'''

        for _ in self.get_fields():

            if to_code == 1:
                pass

            elif to_code == 2:
                pass