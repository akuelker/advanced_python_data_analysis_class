import xml.etree.ElementTree as ET
import os

def getTree(xmlFile):
    #find directory I am currently in
    base_path = os.path.dirname(os.path.realpath(__file__))
    xml_file = base_path + "\\" + fileName #need double slashes to find things properly
    tree = ET.parse(xml_file) 
    return tree

def printAttributes(properties):
    for key, value in properties.items(): #like a dictionary
        print(key, ":", value)
        
def readXML(catalog_root):
    for child in catalog_root:
        printAttributes(child.attrib)
        for element in child:
            print(element.tag, ":",
                  element.text)
            if (element.attrib):
                printAttributes(element.attrib)
        print()

  #add product subelements
def addProduct(catalog_root, skuDict, itemDict, inStore = None):
    new_product = ET.SubElement(catalog_root, "product",
                                attrib = skuDict)
    for key, value in itemDict.items():
        if (inStore) and key == "price":
            new_prod_item = ET.SubElement(new_product, key,
                                          attrib = inStore)
        else:
            new_prod_item = ET.SubElement(new_product, key)
            new_prod_item.text = value
            

#Main Program
fileName = 'Product_Listing.xml'       
tree = getTree(fileName)
root = tree.getroot()
addProduct(root,{"SKU" : "75770"},
           {"name": "Bradleigh",
            "description": "Sweet Girl",
            "cost": "9058.8",
            "inStore": "no"})
tree.write(fileName)
readXML(root)
