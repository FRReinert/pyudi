---
Project: UDI Library for Python
Author: Fabricio R. Reinert <fabricio.reinert@live.com>
Status: Under Development
---

# Description

An agnostic UDI library designed to support multiple UDI patterns (GS1, HIBCC, ICCBA...)

# Status

Under development.

# Goals of this project

## Parse UDI codes
```py
from pyudi.common import Agency
from pyudi.factory import FactoryUDI

label_one = FactoryUDI.make_udi(Agency.GS1)
label_one.parse(SSCC='0844525700', BATCH_LOT='3110210523790', SERIAL='7260112')

label_two = FactoryUDI.make_udi(Agency.GS1)
label_two.parse('000844525700103110210523790217260112')
```

## Serialize an instance

```python
from pyudi.common import Agency, Label
from pyudi.factory import FactoryUDI

label = FactoryUDI.make_udi(Agency.GS1)
label.serialize(human_readable=True)
# >> (00)0844525700(10)3110210523790(21)7260112

label.serialize(label=Label.GS1_DATAMATRIX, human_readable=False)
# >> ]d2000844525700\x1d103110210523790\x1d217260112
```

## Validate fields

```python
from pyudi.common import Agency
from pyudi.factory import FactoryUDI

label = FactoryUDI.make_udi(Agency.GS1)
label.parse(GTIN='7890844525700', BATCH_LOT='000001', SERIAL='7260ZZZ')

label.fieldset.validate()
# Exception('GTIN: Too many chars') ...
```

## Request Info from web

```python
from pyudi.common import Agency
from pyudi.factory import FactoryUDI

label = FactoryUDI.make_udi(Agency.GS1)
label.parse(GTIN='7890844525700', BATCH_LOT='000001', SERIAL='7260ZZZ')

label.fetch_remote_data()
# >> {
#   'enrollment_link': 'https://www...',
#   'product_info': '...',
#   'Manufacturer: '...',
# } 
```
