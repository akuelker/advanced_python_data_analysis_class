import os
import xml.etree.ElementTree as ET

base_path = os.path.dirname(os.path.realpath(__file__))
print(base_path) #for debugging - most common error
xml_file = os.path.join(base_path, 
                        "\\CETC_Catalog.xml")
print(xml_file) #another common error
#Add a root
root = ET.Element("catalog")
tree = ET.ElementTree(root)


#Add a product
new_product = ET.SubElement(root, "product",
                            attrib = {"SKU": "75709"})
new_product_name = ET.SubElement(new_product,
                            "name")

new_product_descrip = ET.SubElement(new_product,
                            "description")
new_product_cost = ET.SubElement(new_product, "price",
                            attrib = 
                            {"inStore":"no"})
new_product_name.text = "Fuzzy Emilia"
new_product_descrip.text = "A cute baby to play with"
new_product_cost.text = "1059.48"
tree.write('Catalog.xml')