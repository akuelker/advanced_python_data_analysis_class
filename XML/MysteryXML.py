import os
import xml.etree.ElementTree as et


def getTree(xmlFile):
    base_path = os.path.dirname(os.path.realpath(__file__))
    xml_file = os.path.join(base_path, xmlFile)
    tree = et.parse(xml_file)
    return tree

def printAttributes(properties):
    for key, value in properties.items():
        print(key, ":", value)
        
def readXML(catalog_root):
    for child in catalog_root:
        printAttributes(child.attrib)
        for element in child:
            print(element.tag, ":", element.text)
            if (element.attrib):
                printAttributes (element.attrib)
        print()

def addUser(cat_root, user, itemDict,
               inStore = None):       
    #subelement must have a parent
    #xml prefers string
    new_product = et.SubElement(
        cat_root, "product", attrib = skuDict)
    
    for key, value in itemDict.items():
        if (inStore) and key == "price":
            new_prod_item = et.SubElement(
                new_product, key, attrib = inStore)
        else:
            new_prod_item = et.SubElement(
                new_product, key)
        new_prod_item.text = value;
         
         
# main code
xmlFile = "ClassData\\CETC_Product_Catalog.xml"
tree = getTree(xmlFile)
readXML(tree.getroot())
pythonDetails = {"name": "Python Fuzzy Snake",
              "description": "A Python snake to welcome "\
                 "your Pythonista friends to your cube",
              "price": "39.95"}
addProduct(tree.getroot(),{"SKU":"41234"},pythonDetails, {"inStore":"no"})
ajaxDetails = {"name": "AJAX",
              "description": "The best cleaner for web applications",
              "price": "2.99"}
addProduct(tree.getroot(),{"SKU":"00112"},ajaxDetails, {"inStore":"yes"})
tree.write(xmlFile)
