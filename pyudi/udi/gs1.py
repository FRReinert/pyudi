from pyudi.common import Agency, Delimiter
from pyudi.fields.gs1 import GS1Fieldset
from pyudi.udi.base import StructureUDI, IStructureUDI


class StructureGS1(StructureUDI, IStructureUDI):
    '''GS1 UDI Representation'''

    agency: Agency = Agency.GS1

    def __init__(self, *args, **kwargs):
        self.fieldset = GS1Fieldset(parent_structure=self, *args, **kwargs)
