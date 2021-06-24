---
Project: UDI Serialization Library for Python
Author: Fabricio Roberto Reinert <fabricio.reinert@live.com>
Status: Not ready for production
---

# Description

This library is designed support UDI patterns and standards in python projects as agnostic as possible. Meaning you can use it with a framework, script, modules or even another library.

# Usage

We are planning to publish it when when it become production ready. Until there, you can clone it and start playing arround with the library.

# Goals

* Serialization

```python
from pyudi.udi import UDIPatternGS1

UDI = UDIPatternGS1('010082700200511217000004101234218234')
print(UDI)
# {"Device Identifier": "00827002005112", "Expiration Date": '000004' ... }

print(UDI.expiration_date)
# 000004
```` 

* Deserialization
```py
UDI = UDIPatternGS1()
UDI.expiration_date = '000004'
UDI.device_identifier = '00827002005112'

print(UDI.human_readable_string)
# (01)00827002005112(17)000004

print(UDI.barcode_string)
# 010082700200511217000004
```

* Validation

```python
UDI = UDIPatternGS1('010082700200511217000004101234218234')
UDI.validate()
# ValidationError('000004' is not a valid Date YYMMDD')
...  
```
