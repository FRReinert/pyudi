from enum import Enum
from collections import namedtuple

GS1_GS = '\x1d'
LabelType = namedtuple("LabelType", "agency fnc1 gs_read_char gs_write_char")


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


class Label:
    GS1_DATAMATRIX = LabelType(Agency.GS1, ']D2', '<GS>', '\x1d')
    GS1_QRCODE = LabelType(Agency.GS1, ']Q3', '<GS>', '\x1d')
    GS1_EAN = LabelType(Agency.GS1, ']E0', '<GS>', '\x1d')
    GS1_128 = LabelType(Agency.GS1, ']C1', '<GS>', '\x1d')
