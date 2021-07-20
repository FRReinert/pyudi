from pyudi.serializers.base import ISerializer
from pyudi.common import Label
from pyudi.fields.base import IField
from typing import Iterable


class Gs1Serializer(ISerializer):

    def serialize_to_human_readable_str(self, fixed_fields: Iterable[IField], variable_fields: Iterable[IField]) -> str:
        '''Transform fields in UDI code'''

        udi = str()

        for field in fixed_fields:
            udi += '(' + field.data_delimiter + ')' + str(field.value)

        for field in variable_fields:
            udi += '(' + field.data_delimiter + ')' + str(field.value)

        return udi

    def serialize_to_barcode_str(self, label: Label, fixed_fields: Iterable[IField], variable_fields: Iterable[IField]) -> str:
        '''Transform fields in UDI code'''

        udi = label.fnc1_write_char

        for field in fixed_fields:
            udi +=  field.data_delimiter + str(field.value)

        for field in variable_fields:
            udi += field.data_delimiter + str(field.value) + label.gs_write_char

        # Remove <GS> from last field
        if udi[-1] == label.gs_write_char:
            udi = udi[:-1]

        return udi