from pyudi.udi import udi
from pyudi.common import Agency

# Parsing GS1 UDI
gs1_obj = udi.FactoryUDI.make_udi(agency=Agency.GS1)
gs1_obj.parse('010844525700213110210523790117260112')

gs1_obj.field_SSCCField  # Return Serial number
gs1_obj.field_GTINField  # Return GTIN
gs1_obj.field_GTINField = '78900010000000'  # Change the field data
gs1_obj.human_readable_str  # Return (01)78900010000000(14)00000(21)00000
gs1_obj.encoded_str = '017890001000000014000002100000'