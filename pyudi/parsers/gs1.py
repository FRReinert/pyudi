from pyudi.parsers.base import IParser
from pyudi.fieldsets.gs1 import GS1Fieldset
from pyudi.common import Label
from typing import Generator


class Gs1Parser(IParser):
    '''Parses and serializes GS1 Fields'''

    def parse_from_barcode(self, label: Label, database_str: str, fieldset: GS1Fieldset) -> Generator:
        '''Parse from UDI code'''

        # Remove FNC1
        if database_str.startswith(label.fnc1):
            barcode_wt_fnc1 = database_str.split(label.fnc1)[1]
        else:
            barcode_wt_fnc1 = database_str

        # Split variable and fixed size fields
        # The 1st element will be the fixed size fields
        # the others are variable size fields
        barcode_split = barcode_wt_fnc1.split(label.gs)
        barcode_fixed_fields = barcode_split[0]
        barcode_var_fields = barcode_split[1:]

        # Parse fixed size fields
        for field in fieldset.get_fixed_size_fields(show_empty=True):
            
            if barcode_fixed_fields.startswith(field.data_delimiter):
                ai = len(field.data_delimiter)-1
                size = field.data_size
                yield field(barcode_fixed_fields[ai:size])
                
                # Remove it from <barcode_fixed_fields>
                barcode_fixed_fields = barcode_fixed_fields[ai + size:]

                # Break loop if <barcode_fixed_fields> is entirely parsed
                if len(barcode_fixed_fields) < 1:
                    break
        
        # Parse variable size fields
        for field in fieldset.get_variable_size_fields(show_empty=True):

            if barcode_var_fields[0].startswith(field.data_delimiter):
                ai = len(field.data_delimiter)-1
                barcode_var_fields[0].replace(label.gs, "")
                yield field(barcode_var_fields[0])

                # Remove it from <barcode_var_fields>
                barcode_var_fields.pop(0)

                # Break loop if <barcode_fixed_fields> is entirely parsed
                if len(barcode_fixed_fields) < 1:
                    break

    def parse_from_parameters(self, **fields) -> Generator:
        '''Parse from kwarg parameters'''
        supplied_parameters = fields.keys()
        for identifier_name, identifier_class in self.fieldset_object.fields.items():
            if identifier_name in supplied_parameters:
                yield identifier_name, identifier_class(fields[identifier_name])

    def serialize(self, label: Label, human_readable: bool) -> str:
        '''Transform fields in UDI code'''

        udi = str()

        if human_readable:
            for field in self.get_fields(show_empty=False):
                udi += '(' + field.data_delimeter + ')' + field.value

        else:
            udi += label.fnc1
            for field in self.get_fields(show_empty=False):
                udi += label.gs + field.data_delimiter + field.value

        return udi
