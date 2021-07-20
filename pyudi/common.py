from enum import Enum
from dataclasses import dataclass


class Agency(Enum):
    '''Valid Agencies'''

    GS1  = 1
    HIBCC = 2
    ICCBBA = 3


class Identifiers:
    '''Supported UDI AIs'''

    SSCC = 'SSCC'
    GTIN = 'GTIN'
    CONTENT = 'CONTENT'
    BATCH_LOT = 'BATCH_LOT'
    PROD_DATE = 'PROD_DATE'
    DUE_DATE = 'DUE_DATE'
    PACK_DATE = 'PACK_DATE'
    BEST_BEFORE_OR_BEST_BY = 'BEST_BEFORE_OR_BEST_BY'
    SELL_BY = 'SELL_BY'
    USE_BY_OR_EXPIRY = 'USE_BY_OR_EXPIRY'
    VARIANT = 'VARIANT'
    SERIAL = 'SERIAL'
    CPV = 'CPV'


@dataclass
class _LABELTYPE:
    agency: Agency
    fnc1_read_char: str
    fnc1_write_char: str
    gs_read_char: str
    gs_write_char: str


class Label:
    GS1_DATAMATRIX = _LABELTYPE(Agency.GS1, ']D2', '\xe8', '<GS>', '\x1d')
    GS1_QRCODE = _LABELTYPE(Agency.GS1, ']Q3', '', '<GS>', '\x1d')  # TODO: Add ASCII Write FNC1
    GS1_EAN = _LABELTYPE(Agency.GS1, ']E0', '', '<GS>', '\x1d')  # TODO: Add ASCII Write FNC1
    GS1_128 = _LABELTYPE(Agency.GS1, ']C1', '', '<GS>', '\x1d')  # TODO: Add ASCII Write FNC1
