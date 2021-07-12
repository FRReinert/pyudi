from typing import Any
from pyudi.common import Agency
from pyudi.udi.gs1 import StructureGS1
from pyudi.fields.gs1 import *


class FactoryUDI:
    '''UDI Factory'''

    @staticmethod
    def make_udi(agency: Agency, **kwargs) -> Any:
        '''Create UDI instance our of fields'''
        
        if agency == Agency.GS1:
            instance = StructureGS1(**kwargs)
        
        elif agency == Agency.HIBCC:
            raise NotImplementedError
        
        elif agency == Agency.ICCBBA:
            raise NotImplementedError

        return instance

    @staticmethod
    def make_udi_by_parse(agency: Agency, database_field: str) -> Any:
        '''Create UDI instance out of a database string'''

        if agency == Agency.GS1:
            structure = StructureGS1(database_field=database_field)
        
        elif agency == Agency.HIBCC:
            raise NotImplementedError
        
        elif agency == Agency.ICCBBA:
            raise NotImplementedError
              
        return structure
