from pyudi.common import Agency, Label
from pyudi.fields.gs1 import GS1Fieldset, Gs1Parser
from pyudi.fieldsets.gs1 import GS1Fieldset
from pyudi.parsers.gs1 import Gs1Parser
from pyudi.udi.base import StructureUDI, IStructureUDI


class StructureGS1(StructureUDI, IStructureUDI):
    '''GS1 UDI Representation'''

    def __init__(self, **kwargs) -> None:
        self.agency = Agency.GS1
        self.fieldset = GS1Fieldset()
        self.parser = Gs1Parser()
    
    def parse(self, database_str: str, **kwargs) -> None:
        '''Parsing fields'''

        if database_str:
            for ai, field_instance in self.parser.parse_from_barcode(database_str):
                setattr(self.fieldset, ai, field_instance)
        else:
            for ai, field_instance in self.parser.parse_from_parameters(**kwargs):
                setattr(self.fieldset, ai, field_instance)

    def serialize(self, label: Label, human_readable=bool) -> str:
        '''Call Parser to serialize fields'''

        if label.agency != self.agency:
            raise TypeError(f'Label {label} cant be used with {self.agency} structure')

        return self.parser.serialize(human_readable=human_readable, label=label)
