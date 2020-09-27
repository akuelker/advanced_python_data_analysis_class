import os
import xml.etree.ElementTree as et
 # directory of file being run
base_path = os.path.dirname(os.path.realpath(__file__))
print(base_path)
xml_file = os.path.join(base_path, "ClassData\\CETC_Product_Catalog.xml")
print(xml_file)
#saves XML file in memory
tree = et.parse(xml_file)
#tree is an object. getroot is a method
root = tree.getroot()
#subelement must have a parent
#xml prefers string
new_product = et.SubElement(root, "product", attrib = {"SKU":"41234"})
new_prod_name = et.SubElement(new_product, "name")
new_prod_desc = et.SubElement(new_product, "description")
new_prod_cost = et.SubElement(new_product, "price", attrib = {"inStore":"no"})

new_prod_name.text = "Python Fuzzy Snake"
new_prod_desc.text = "A Python snake to welcome your Pythonista friends to your cube"
new_prod_cost.text = "39.95"

#writes this on the old xml file
tree.write(xml_file)

