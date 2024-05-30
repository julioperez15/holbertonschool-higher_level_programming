import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    # Create the root element
    root = ET.Element("data")
    
    # Iterate through dictionary items and add them as child elements
    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)
    
    # Create an ElementTree object and write to a file
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()
    
    # Construct the dictionary
    result = {}
    for child in root:
        result[child.tag] = child.text
        
    return result
