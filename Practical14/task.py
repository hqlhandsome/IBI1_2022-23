from xml.dom.minidom import parse
import xml.dom.minidom
import re
import openpyxl
from openpyxl.styles import Font

# Parse the XML file using xml.dom.minidom
DOMTree = xml.dom.minidom.parse("go_obo.xml")
term = DOMTree.documentElement
terms = term.getElementsByTagName("term")

# Create a dictionary to store parent-child relations between GO terms
parent_child_relations = {}

# Create an empty list to store rows of data for the Excel file
rows = []

# Iterate over each "term" element in the XML document
for term in terms:
    # Extract the GO ID of the current term
    go_id = term.getElementsByTagName("id")[0].childNodes[0].data

    # Retrieve the "is_a" elements within the current term
    is_a_elements = term.getElementsByTagName("is_a")
    
    # Iterate over each "is_a" element
    for is_a_element in is_a_elements:
        # Extract the GO ID of the parent term
        is_a_id = is_a_element.childNodes[0].data
        
        # Add the parent-child relation to the dictionary
        if is_a_id not in parent_child_relations:
            parent_child_relations[is_a_id] = []
        parent_child_relations[is_a_id].append(go_id)

# Iterate over each "term" element again
for term in terms:
    # Extract the "defstr" element and its data
    defstr = term.getElementsByTagName("defstr")[0].childNodes[0].data
    
    # Search for the pattern 'autophagosome' within the definition
    match_autophagosome = re.search('autophagosome', defstr)
    
    # If there is a match, extract the relevant information
    if match_autophagosome:
        go_id = term.getElementsByTagName("id")[0].childNodes[0].data
        name = term.getElementsByTagName("name")[0].childNodes[0].data
        is_a_count = len(parent_child_relations.get(go_id, []))
        child_nodes = parent_child_relations.get(go_id, [])
        
        # Append the extracted information to the rows list
        rows.append([go_id, name, defstr, is_a_count])
        
        # Print the extracted information to the console
        print("GO_id:", go_id)
        print("Term_Name:", name)
        print("Definition:", defstr)
        print("ChildNodes:", is_a_count)
        print("ChildNodes are:", child_nodes)
        print()

# Create a new Excel workbook
workbook = openpyxl.Workbook()
sheet = workbook.active

# Append the header row to the sheet
sheet.append(["Go_id", "Name", "Definition", "Childnodes"])

# Apply bold font style to the header cells
bold_font = Font(bold=True)
for cell in sheet[1]:
    cell.font = bold_font

# Append the rows of data to the sheet
for row in rows:
    sheet.append(row)

# Save the workbook as "autophagosome.xlsx"
workbook.save("autophagosome.xlsx")
