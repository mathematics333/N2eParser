from lxml import etree

def extract_view_names(file_path):
    """
    Extracts the "name" attribute from tags that start with <view name= in the XML file.
    """
    view_names = []
    
    # Parse the XML file
    parser = etree.XMLParser(recover=True)  # Using recover mode to handle errors
    tree = etree.parse(file_path, parser)
    root = tree.getroot()

    # Iterate through all elements in the XML
    for elem in root.iter():
        # Check if the element is a 'view' element and has a 'name' attribute
        if 'view' in elem.tag and 'name' in elem.attrib:
            view_names.append(elem.attrib['name'])
    
    return view_names

# Path to the XML file
file_path = '20231026.xml'

# Extracting view names from the XML file
view_names = extract_view_names(file_path)
print(view_names)
