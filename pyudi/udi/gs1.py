from pyudi.common import Agency, Label
from pyudi.fieldsets.gs1 import GS1Fieldset
from pyudi.parsers.gs1 import Gs1Parser
from pyudi.udi.base import StructureUDI, IStructureUDI


class StructureGS1(StructureUDI, IStructureUDI):
    '''GS1 UDI Representation'''

    def __init__(self) -> None:
        self.agency = Agency.GS1
        self.fieldset = GS1Fieldset()
        self.parser = Gs1Parser()
    
    def parse(self, database_str: str = None, label: Label = None, **kwargs) -> None:
        '''Parsing fields into composed fieldset object'''

        if database_str:
            if label == None:
                raise TypeError('Missing required parameter <Label>')

            for field_instance in self.parser.parse_from_barcode(label, database_str, self.fieldset):
                setattr(self.fieldset, field_instance.name, field_instance)
        else:
            for field_instance in self.parser.parse_from_parameters(self.fieldset.fields, **kwargs):
                setattr(self.fieldset, field_instance.name, field_instance)

    def serialize(self, human_readable: bool, label: Label = None) -> str:
        '''Serialize fields into string'''

        serialized = str()

        if label.agency != self.agency:
            raise TypeError(f'Label {label} cant be used with {self.agency} structure')

        fixed_size_fields = self.fieldset.get_fixed_size_fields(show_empty_fields=False)
        variable_size_fields = self.fieldset.get_variable_size_fields(show_empty_fields=False)

        if human_readable:
            serialized = self.parser.serialize_to_human_readable_str(fixed_size_fields, variable_size_fields)
        
        else:
            serialized = self.parser.serialize_to_barcode_str(fixed_size_fields, variable_size_fields)
        
        return serialized
