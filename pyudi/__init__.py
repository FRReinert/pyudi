'''
This Package is provided under MIT License and is free to use and change.
It is mainly applicable to projects which need Serialization/Deserialization of UDI codes
'''

__version__ = '0.0.1'
__license__ = "MIT"
__copyright__ = "Copyright 2021, Python UDI Serializer Library"
__status__ = 'Development'
__author__ = 'Fabricio Roberto Reinert'
__email__ = "fabricio.reinert@live.com"
__maintainer__ = "Fabricio Roberto Reinert"

if __name__ == '__main__':

    from pyudi.common import Agency, Label
    from pyudi.factory import FactoryUDI

    # Example 1
    gs1 = FactoryUDI.make_udi(Agency.GS1)
    gs1.parse(GTIN='07897990308239', BATCH_LOT='3110210523790', SERIAL='7260112')
    
    print(gs1.serialize(label=Label.GS1_DATAMATRIX, human_readable=False))
    print(gs1.serialize(label=Label.GS1_DATAMATRIX, human_readable=True))