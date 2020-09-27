import os
import xml.etree.ElementTree as et
 # directory of file being run
base_path = os.path.dirname(os.path.realpath(__file__))
print(base_path)
xml_file = os.path.join(base_path, "data\\Product_Listing.xml")
print(xml_file)
#saves XML file in memory
tree = et.parse(xml_file)
#tree is an object. getroot is a method
root = tree.getroot()
#getting a list
for child in root:
    print(child.tag, child.attrib)  #prints out product
#lists everything    
for child in root:
    for element in child:
        print(element.tag, ":", element.text)
#subelement must have a parent
#xml prefers string
new_product = et.SubElement(root, "product", attrib = {"id":"4"})
new_prod_name = et.SubElement(new_product, "name")
new_prod_desc = et.SubElement(new_product, "description")
new_prod_cost = et.SubElement(new_product, "cost")
new_prod_ship = et.SubElement(new_product, "shipping")

new_prod_name.text = "Python Pants"
new_prod_desc.text = "These pants will surely help you code like crazy!"
new_prod_cost.text = "39.95"
new_prod_ship.text = "4.00"
#writes this on the old xml file
tree.write(xml_file)
