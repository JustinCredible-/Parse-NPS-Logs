import xml.etree.ElementTree as ET
import pandas as pd

# Path to your XML file
file_path = 'path_to_your_file.log'

# Read the file content
with open(file_path, 'r') as file:
    content = file.read()

# Wrap the content in a root tag (if not already present)
content = '<Events>' + content + '</Events>'

# Parse the XML content
root = ET.fromstring(content)

# List to hold all event data
data = []

# Parsing each event and its child elements
for event in root.findall('Event'):
    event_data = {}
    for child in event:
        event_data[child.tag] = child.text.strip() if child.text else ''
    data.append(event_data)

# Converting the data into a DataFrame
df = pd.DataFrame(data)

# Creating an HTML file with alternating row colors
html_content = df.to_html(classes='table table-striped', escape=False, index=False)

# CSS for alternating row colors
css = """
<style>
    .table-striped tbody tr:nth-of-type(odd) {
        background-color: #f9f9f9;
    }
</style>
"""

# Full HTML content
html_full_content = css + html_content

# Path for the HTML output file
html_file_path = 'path_to_output_file.html'

# Save to HTML file
with open(html_file_path, 'w') as f:
    f.write(html_full_content)
