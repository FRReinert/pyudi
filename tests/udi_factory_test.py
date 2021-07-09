import unittest
from pyudi.common import Agency
from pyudi.factory import FactoryUDI


class TestUDIFactory(unittest.TestCase):
    
    gs1_ex1 = FactoryUDI.make_udi(Agency.GS1, SSCCField='0844525700', BatchLotField='3110210523790', SerialNumberField='7260112')
    gs1_ex2 = FactoryUDI.make_udi_by_parse(Agency.GS1, '010844525700213110210523790117260112')


unittest.main()
