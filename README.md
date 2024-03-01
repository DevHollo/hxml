# hxml
hxml is a simple xml parser for Python 3.12<br/>

## Examples
```xml
<!-- test.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<le_epic_xml>
    <name>Epic XML</name>
    <cool>
        <a>as</a>
        <b>you</b>
        <c>see</c>
        <d>it</d>
        <e>works!</e>
    </cool>
</le_epic_xml>
```
```py
# epic_xml.py
from hxml import XML

xml = XML("test.xml").get_root_item("le_epic_xml")

print(xml) # output: {'name': 'Epic XML', 'cool': {'a': 'as', 'b': 'you', 'c': 'see', 'd': 'it', 'e': 'works!'}}
```
