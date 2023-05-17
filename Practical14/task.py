from xml.dom.minidom import parse
import xml.dom.minidom
import re
import openpyxl
from openpyxl.styles import Font

def count_child_nodes(go_id, parent_child_relations):
    # Helper function to calculate the number of child nodes for a given GO ID

    if go_id not in parent_child_relations:
        return 0

    child_nodes = parent_child_relations[go_id]
    count = len(child_nodes)

    for child_node in child_nodes:
        # Recursively call count_child_nodes() to calculate the number of child nodes of the child nodes
        count += count_child_nodes(child_node, parent_child_relations)

    return count


DOMTree = xml.dom.minidom.parse("go_obo.xml")
term = DOMTree.documentElement
terms = term.getElementsByTagName("term")

parent_child_relations = {}
rows = []

# First iteration: Build the parent-child relations dictionary
for term in terms:
    go_id = term.getElementsByTagName("id")[0].childNodes[0].data
    is_a_elements = term.getElementsByTagName("is_a")
    for is_a_element in is_a_elements:
        is_a_id = is_a_element.childNodes[0].data
        if is_a_id not in parent_child_relations:
            parent_child_relations[is_a_id] = []
        parent_child_relations[is_a_id].append(go_id)

# Second iteration: Process terms with "autophagosome" condition
for term in terms:
    defstr = term.getElementsByTagName("defstr")[0].childNodes[0].data
    match_autophagosome = re.search('autophagosome', defstr)
    if match_autophagosome:
        go_id = term.getElementsByTagName("id")[0].childNodes[0].data
        name = term.getElementsByTagName("name")[0].childNodes[0].data
        is_a_count = count_child_nodes(go_id, parent_child_relations)

        child_nodes = parent_child_relations.get(go_id, [])
        rows.append([go_id, name, defstr, is_a_count])


# Create an Excel workbook and save the data
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.append(["Go_id", "Name", "Definition", "Childnodes"])

bold_font = Font(bold=True)

# Set the font of the header row to bold
for cell in sheet[1]:
    cell.font = bold_font

# Add the data to the worksheet
for row in rows:
    sheet.append(row)

workbook.save("autophagosome.xlsx")
