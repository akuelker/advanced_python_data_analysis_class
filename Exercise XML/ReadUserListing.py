import os
import xml.etree.ElementTree as et
#from  printNiceXML import printNiceXML

def printXML(root):
    for child in root:
        for element in child:
            print(element.tag, ":", element.text)
            if (element.attrib):
                printAttributes (element.attrib)
        print()
def printAddress(root):
    for child in root:
        name = ""; apt = ""; address = ""; cityStateZip = "";
        for element in child:
            if (element.tag in ["firstName", "lastName"]):
                name += element.text + " "
            elif (element.tag in ["apartment"]):
                  apt = element.text
            elif (element.tag in ["street"]):
                  address = element.text
            elif (element.tag in ["city", "state", "zip"]):
                  cityStateZip +=element.text
        print(name)
        if len(apt) > 0:
            print(apt)
        print(address)
        print(cityStateZip)
        print() #to separate addresses

def getEmail(tree):
    emailElements = tree.findall('User/email')
    emailList = []
    print("The number of emails are: %d"
          %len(emailElements))
    for element in emailElements:
        #print(element.tag, ":", element.text)
        emailList.append(element.text)
    return(emailList)
#main code
base_path = os.path.dirname(os.path.realpath(__file__))
xml_file = os.path.join(base_path, "UserList.xml")
#XML file saved in memory
tree = et.parse(xml_file)
#Find the root of the tree (which should be users)
root = tree.getroot()
emailList = getEmail(tree)
print(emailList)
