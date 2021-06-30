from pyudi.fields.factory import FieldFactoryGs1
from pyudi.udi.gs1 import StructureGS1


class FactoryUDI:
    '''UDI Factory'''

    @staticmethod
    def create_gs1(database_udi: str) -> StructureGS1:
        '''Create GS1 UDI instance'''
        instance = StructureGS1()
        for field, value in FieldFactoryGs1.create_fields(database_udi):
            setattr(instance, field.name, field(agency='gs1', value=value))
        return instance
