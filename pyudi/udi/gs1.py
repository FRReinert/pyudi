from pyudi.common import Agency
from pyudi.fields.gs1 import GS1Fieldset
from pyudi.udi.base import IStructureUDI


class StructureGS1(IStructureUDI):
    '''GS1 UDI Representation'''

    agency: Agency = Agency.GS1

    def __init__(self, *args, **kwargs):
        self.fieldset = GS1Fieldset(*args, **kwargs)
