from enum import Enum
from collections import namedtuple

GS1_GS = '\x1d'


class Agency(Enum):
    '''Valid Agencies'''

    GS1  = 1
    HIBCC = 2
    ICCBBA = 3


_label = namedtuple("Label", "agency fnc1 gs")
class Label(Enum):
    GS1_DATAMATRIX = _label(Agency.GS1, ']D2', '\x1d')
    GS1_QRCODE = _label(Agency.GS1, ']Q3', '\x1d')
    GS1_EAN = _label(Agency.GS1, ']E0', '\x1d')
    GS1_128 = _label(Agency.GS1, ']C1', '\x1d')


class Identifiers(Enum):
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
