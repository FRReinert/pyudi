from typing import Any
from pyudi.common import Agency, Delimiter
from pyudi.udi.gs1 import StructureGS1
from pyudi.udi.base import IStructureUDI
from pyudi.fields.gs1 import *


class FactoryUDI:
    '''UDI Factory'''

    @staticmethod
    def make_udi(agency: Agency) -> IStructureUDI:
        '''Create UDI instance our of fields'''

        if agency == Agency.GS1:
            instance = StructureGS1()

        elif agency == Agency.HIBCC:
            raise NotImplementedError

        elif agency == Agency.ICCBBA:
            raise NotImplementedError

        return instance
