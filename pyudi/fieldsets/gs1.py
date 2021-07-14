from pyudi.fieldsets.base import Fieldset, IFieldset
from pyudi.fields.gs1 import *

class GS1Fieldset(IFieldset, Fieldset):
    '''Represent a container with GS1 Fields'''

    def __init__(self):

        # Identifier Class for GS1
        self.fields = {
            'SSCC':SSCCField, 'GTIN':GTINField, 'CONTENT':ContentField, 'BATCH_LOT':BatchLotField, 
            'PROD_DATE':ProductionDateField, 'DUE_DATE':ExpiringDateField, 'PACK_DATE':PackingDateField,
            'BEST_BEFORE_OR_BEST_BY':MinimalExpiringField, 'SELL_BY':SellExpiringField, 'USE_BY_OR_EXPIRY':MaxExpiringDateField,
            'VARIANT':InternalProductVariantField, 'SERIAL':SerialNumberField, 'CPV':ConsumerProductVariantField
        }

        # Initialize Fields with null value
        self.initialize_fields()
