#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

# what is this?
# this takes a mailFilters.xml file generated from exporting your gmail filters
# and modifies the archive function to true\false\foo
# why?
# So I can switch my on call filters, when I go on\off rotation.

xml_input = sys.argv[1] if len(sys.argv) > 1 else "mailFilters.xml"
search_value = sys.argv[2] if len(sys.argv) > 2 else "oncall"
update_value = sys.argv[3] if len(sys.argv) > 3 else "true"
update_file_name = sys.argv[4] if len(sys.argv) > 4 else "mailFilters-updated.xml"

namespaces = {str(x[0]) if x[0] != "" else "atom": x[1] for _, x in ET.iterparse(xml_input, events=['start-ns'])}

for k in namespaces:
    ET.register_namespace(k, namespaces[k])

tree = ET.parse(xml_input)
root = tree.getroot()

for e in root.findall("./atom:entry", namespaces):
    labels = e.find("./apps:property[@name='label']", namespaces)
    if labels is not None:
        label_text = labels.attrib['value']
        if search_value in label_text:
            should_archive = e.find("./apps:property[@name='shouldArchive']", namespaces)
            if should_archive is not None:
                should_archive.attrib['value'] = update_value
            else:
                child = ET.SubElement(e, '{http://schemas.google.com/apps/2006}property')
                child.attrib['name'] = 'shouldArchive'
                child.attrib['value'] = update_value

ET.ElementTree(root).write(update_file_name)