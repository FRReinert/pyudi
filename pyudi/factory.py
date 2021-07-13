from typing import Any
from pyudi.common import Agency, Delimiter
from pyudi.udi.gs1 import StructureGS1
from pyudi.fields.gs1 import *


class FactoryUDI:
    '''UDI Factory'''

    @staticmethod
    def make_udi(agency: Agency, delimiter: Delimiter, **kwargs) -> Any:
        '''Create UDI instance our of fields'''

        if delimiter == Delimiter.AUTO:
            delimiter = Delimiter.FNC1_GS
        
        if agency == Agency.GS1:
            instance = StructureGS1(delimiter=delimiter, **kwargs)
        
        elif agency == Agency.HIBCC:
            raise NotImplementedError
        
        elif agency == Agency.ICCBBA:
            raise NotImplementedError

        return instance

    @staticmethod
    def make_udi_from_encoded_string(agency: Agency, delimiter: Delimiter, database_field: str) -> Any:
        '''Create UDI instance out of a database string'''

        # Verify AUTO delimiter
        if delimiter == Delimiter.AUTO:
            if '\x1d' in database_field:
                delimiter = Delimiter.FNC1_GS
            else:
                delimiter == Delimiter.AI_SIZE

        if agency == Agency.GS1:
            instance = StructureGS1(delimiter=delimiter, database_field=database_field)

        elif agency == Agency.HIBCC:
            raise NotImplementedError

        elif agency == Agency.ICCBBA:
            raise NotImplementedError

        return instance
