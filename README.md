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

label_one = FactoryUDI.make_udi(Agency.GS1, SSCC='0844525700', BATCH_LOT='3110210523790', SERIAL='7260112')

label_two = FactoryUDI.make_udi_by_parse(Agency.GS1, '000844525700103110210523790217260112')
```

## Serialize an instance

```python
from pyudi.common import Agency
from pyudi.factory import FactoryUDI

label = FactoryUDI.make_udi(Agency.GS1, SSCC='0844525700', BATCH_LOT='3110210523790', SERIAL='7260112')

label.fieldset.parser.serialize(human_readable=True)
# >> (00)0844525700(10)3110210523790(21)7260112

label.fieldset.parser.serialize(human_readable=False)
# >> \x1d000844525700\x1d103110210523790\x1d217260112
# 0x1D is the Data Delimiter
```

## Validate fields

```python
from pyudi.common import Agency
from pyudi.factory import FactoryUDI

label = FactoryUDI.make_udi(Agency.GS1, GTIN='7890844525700', BATCH_LOT='000001', SERIAL='7260ZZZ')

label.fieldset.validate()
# Exception('GTIN: Too many chars') ...
```

## Request Info from web

```python
from pyudi.common import Agency
from pyudi.factory import FactoryUDI

label = FactoryUDI.make_udi(Agency.GS1, GTIN='7890844525700', BATCH_LOT='000001', SERIAL='7260ZZZ')

label.http.to_dict()
# >> {
#   'enrollment_link': 'https://www...',
#   'product_info': '...',
#   'Manufacturer: '...',
# } 
```
