from pyudi.udi.base import IBaseUDI
from pyudi.fields import gs1


class GS1Pattern(IBaseUDI):
    '''UDI Class for GS1 Pattern'''

    encoded_udi_string = ''
    human_readable_udi_string = ''

    def __init__(self, barcode: str = None, human_readable: str = None):
        if barcode or human_readable:
            self.encode_udi(barcode=barcode, human_readable=human_readable)

    def encode_udi(self, barcode: str = None, human_readable: str = None) -> None:
        '''Try to encode data from humanized/barcode string'''

        if barcode:
            for field in self.field_list(gs1):
                # Barcodes in GS1 dont use '(' or ')' within the string
                pass

        elif human_readable:
            for field in self.field_list(gs1):
                # Human readable UDI in GS1 use '(' and ')' to encapsulate data limiter
                pass

        else:
            raise TypeError('Missing parameters: <barcode> OR <human_readable>')

    def decode_udi(self) -> str:
        '''Convert instance in barcode/humanized string'''
        pass
