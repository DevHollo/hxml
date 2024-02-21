from hxml import XML

xml = XML("test.xml")

epic_xml = xml.get("le_epic_xml")
print(epic_xml) # output: {'name': 'Epic XML', 'cool': {'a': 'as', 'b': 'you', 'c': 'see', 'd': 'it', 'e': 'works!'}}