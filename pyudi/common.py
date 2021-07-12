from enum import Enum


class Agency(Enum):
    '''Valid Agencies'''

    GS1  = 1
    HIBCC = 2
    ICCBBA = 3


class Identifiers(Enum):
    '''Supported UDI Identifiers'''

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
