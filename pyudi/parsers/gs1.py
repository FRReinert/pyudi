from pyudi.parsers.base import IParser
from pyudi.fields.base import IField
from pyudi.fieldsets.gs1 import GS1Fieldset
from pyudi.common import Label
from typing import Iterator


class Gs1Parser(IParser):
    '''Parses and serializes GS1 Fields'''

    def parse_from_barcode(self, database_str: str, label: Label, fieldset: GS1Fieldset) -> Iterator:
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
        while True:
            for field_class in fieldset.get_fixed_size_fields(show_empty_fields=True):
                
                if barcode_fixed_fields.startswith(field_class.data_delimiter):
                    ai_size = len(field_class.data_delimiter)
                    data_size = field_class.data_size
                    
                    value = barcode_fixed_fields[ai_size : data_size]
                    field_obj = field_class(value)

                    # TODO: Run validations here!

                    yield field_obj
                    
                    # Remove it from <barcode_fixed_fields>
                    barcode_fixed_fields = barcode_fixed_fields[(ai_size + data_size)-1 : ]
                    
                    # Force FOR loop to restart and re-check all fields
                    break

            # Break loop if <barcode_fixed_fields> is entirely parsed
            if len(barcode_fixed_fields) < 1:
                break
        
        # Parse variable size fields
        while True:
            for field in fieldset.get_variable_size_fields(show_empty_fields=True):

                if barcode_var_fields[0].startswith(field.data_delimiter):
                    ai_size = len(field.data_delimiter)
                    value = barcode_var_fields[0][ai_size:]
                    field_obj = field(value)
                    
                    # TODO: Run validations here!
                    
                    yield field_obj

                    # Remove it from <barcode_var_fields>
                    barcode_var_fields.pop(0)

                    # Force FOR loop to restart and re-check all fields
                    break

            # Break loop if <barcode_fixed_fields> is entirely parsed
            if len(barcode_var_fields) < 1:
                break

    def parse_from_parameters(self, fieldset_clases: dict[str, IField], **kwargs) -> Iterator:
        '''Parse from kwarg parameters'''

        supplied_parameters = kwargs.keys()
        
        for identifier_name, identifier_class in fieldset_clases.items():
            
            if identifier_name in supplied_parameters:
                value = kwargs[identifier_name]
                field_obj = identifier_class(value)

                # TODO: Run validations here!

                yield field_obj

    def serialize_to_human_readable_str(self, fixed_fields: Iterator[IField], variable_fields: Iterator[IField]) -> str:
        '''Transform fields in UDI code'''

        udi = str()

        for field in fixed_fields:
            udi += '(' + field.data_delimeter + ')' + field.value

        for field in variable_fields:
            udi += '(' + field.data_delimeter + ')' + field.value

        return udi

    def serialize_to_barcode_str(self, label: Label, fixed_fields: Iterator[IField], variable_fields: Iterator[IField]) -> str:
        '''Transform fields in UDI code'''

        udi = label.fnc1

        for field in fixed_fields:
            udi +=  field.data_delimiter + field.value

        for field in variable_fields:
            udi += field.data_delimiter + field.value + label.gs

        # Remove <GS> from last field
        if udi[-1] == label.gs:
            udi = udi[:-1]

        return udi
