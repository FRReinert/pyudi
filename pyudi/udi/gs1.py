from pyudi.udi.base import IBaseUDI
from pyudi.fields import gs1


class GS1Pattern(IBaseUDI):
    '''UDI Class for GS1 Pattern'''

    encoded_udi_string = ''
    human_readable_udi_string = ''

    def __init__(self, barcode: str):
        self.encode_udi(barcode = barcode)

    def encode_udi(self, barcode: str) -> None:
        '''Encode data from barcode string'''
            
        for field in self.field_list(gs1):
            # Barcodes in GS1 dont use '(' or ')' within the string
            pass


    def decode_udi(self) -> str:
        '''Convert instance in barcode/humanized string'''
        pass
