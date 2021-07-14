import unittest
from pyudi.common import Agency, Label
from pyudi.factory import FactoryUDI


class TestUDIFactory(unittest.TestCase):
    
    gs1 = FactoryUDI.make_udi(Agency.GS1)
    gs1.parse(Label.GS1_DATAMATRIX, '010844525700<GS>217260112<GS>103110210523790')


unittest.main()
