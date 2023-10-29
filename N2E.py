import pandas as pd
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

def save_to_excel(data, output_file):
    """
    Saves a list of data to an Excel file.
    :param data: List of data to be saved
    :param output_file: Path to the output Excel file
    """
    # Creating a DataFrame from the list
    df = pd.DataFrame(data, columns=['View Name'])
    
    # Saving the DataFrame to an Excel file
    df.to_excel(output_file, index=False)

# Path to the XML file
file_path = 'NwInput.xml'

# Extracting view names from the XML file
view_names = extract_view_names(file_path)

# Saving the extracted view names to an Excel file
save_to_excel(view_names, 'NwOutput.xlsx')
