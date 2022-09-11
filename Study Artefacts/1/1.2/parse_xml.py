import xmltodict

with open("xml.xml") as data:
    xml_data = data.read()

xml_dict = xmltodict.parse(xml_data)
print(xml_dict)
print(type(xml_dict))