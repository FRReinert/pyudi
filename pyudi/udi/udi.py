from pyudi.common import Agency
from pyudi.fields.gs1 import *
from pyudi.udi.base import IStructureUDI
from dataclasses import dataclass
from typing import Optional

@dataclass
class StructureGS1(IStructureUDI):
    '''GS1 UDI Representation'''

    field_SSCCField: Optional[SSCCField]
    field_GTINField: Optional[GTINField]
    field_ContentField: Optional[ContentField]
    field_BatchLotField: Optional[BatchLotField]
    field_ProductionDateField: Optional[ProductionDateField]
    field_ExpiringDateField: Optional[ExpiringDateField]
    field_PackingDateField: Optional[PackingDateField]
    field_MinimalExpiringField: Optional[MinimalExpiringField]
    field_SellExpiringField: Optional[SellExpiringField]
    field_MaxExpiringDateField: Optional[MaxExpiringDateField]
    field_InternalProductVariantField: Optional[InternalProductVariantField]
    field_SerialNumberField: Optional[SerialNumberField]
    field_ConsumerProductVariantField: Optional[ConsumerProductVariantField]
    agency: Agency = Agency.GS1

    def parse(self, database_str: str) -> None:
        '''Parses database <str> to class fields'''
        delimiters = {field.name: field.data_delimiter for field in self.get_fields()}
        for chunk in database_str.split(str(0x29)):
            for field, delimiter in delimiters.items():
                if chunk.startswith(delimiter):
                    pass


class FactoryUDI:
    '''UDI Factory'''

    @staticmethod
    def make_udi(agency: Agency, database_field: str):
        '''Create UDI instance'''
        if agency == Agency.GS1:
            structure = StructureGS1()
        
        structure.parse(database_field)
        
        return structure
