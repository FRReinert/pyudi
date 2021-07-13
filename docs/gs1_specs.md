# GS1 Documents

[GS1 General Specifications](https://www.gs1.org/standards/barcodes-epcrfid-id-keys/gs1-general-specifications)

[GS1 US - Implementation Guideline, Page 38]([https://link](https://www.gs1us.org/DesktopModules/Bring2mind/DMX/Download.aspx?Command=Core_Download&EntryId=390&language=en-US&PortalId=0&TabId=13))


# Encoding Information

## Symbol Character Function 1 (FNC1)

GS1 DataMatrix are initialized with a specific symbol to diferentiate from other agency DataMatrix patterns.
A Character Function 1 (FNC1) is in the first position of the encoded data.

The field separator character is used to control the termination of the field, when its not a fixed size field (some fields sizes can vary others don't).
All fields with variable size must terminate with the field separator character, unless this is the last field in the barcode.

Within the GS1 DataMatrix, the FNC1 is coded in two different ways:

- As the initial character - ASCII 0xe8 - 232: ]d2
- As a field separator - ASCII 0x1D - 29: (Also show as <GS> in some decoders)

## Example of data concatenation


| 0xe8 | AI 1 | Data 1 | AI 2 |  Data 2| 0x1D | AI 3 | Data 3 |
|-----|------|--------|------|--------|------|------|-------|
| FNC1 (initializer) | AI 01 | Fixed Size Field of AI1 | AI 2 02 | Variable size Field | ASCII 29 GS | AI 03 | Data of field 03 |
|Start...|||||||...End|

```python
#!/usr/bin/env python

'''010789835741001571332109876543212112345678901231718123110123ABC'''
encoded = '\xe801078983574100157133210987654321\x1d211234567890123\x1d1718123110123ABC'

```
