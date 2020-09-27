import xml.etree.ElementTree as et
from  printNiceXML import printNiceXML

def createSubElement(child, descrip, text):
    child_part = et.SubElement(child, descrip)
    child_part.text = text

def createUser(user_root):
    child = et.SubElement(user_root, "User")
    #First Name
    firstName = input("Enter your first name")
    createSubElement(child, "firstName", firstName)
##    child_name = et.SubElement(child, "firstName")
##    child_name.text = firstName
    lastName = input("Enter your last name")
    createSubElement(child, "lastName", lastName)
    apartment = input("Enter your apartment "\
                      "address if you have one (return otherwise)")
    if (len(apartment) > 0):
        createSubElement(child, "apartment", apartment)
    street = input("Enter your street number and street")
    createSubElement(child, "street", street)
    city = input("Enter your city")
    createSubElement(child, "city", city)
    state = input("Enter your two letter state")
    createSubElement(child, "state", state)
    zipCode = input("Enter your zipCode")
    createSubElement(child, "zipCode", zipCode)
    email = firstName[0] + lastName
    createSubElement(child, "email", email)
##    print(email) # makes sure email is OK.
    
# main code
user_root = et.Element("users")
ans="N"
count = 0
while not(ans == "y" or ans == "Y"):
    createUser(user_root)
    ans = input("Enter y if finished entering users")
##print(user_root)
##print(et.tostring(user_root))
##print(printNiceXML(user_root))
tree = et.ElementTree(user_root)
tree.write("UserList.xml")

