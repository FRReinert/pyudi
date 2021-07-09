from pyudi.common import Agency
from pyudi.fields.gs1 import GS1Fieldset
from pyudi.udi.base import IStructureUDI


class StructureGS1(IStructureUDI):
    '''GS1 UDI Representation'''

    fieldset: GS1Fieldset
    agency: Agency = Agency.GS1
