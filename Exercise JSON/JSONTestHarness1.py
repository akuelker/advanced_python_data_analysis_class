from JSONCoding1 import *

def checker(item):
    print(type(item), "check.  Value: ", item)
    encodedItem = encode(item)
    decodedItem = decode(encodedItem)
    print(item, ":", item == decodedItem)

def checkerFile(item):
    fileName = "TestHarness.JSON"
    print(type(item), "check.  Value: ", item)
    encodedItem = encode(item, fileName)
    decodedItem = decodeFile(fileName)
    print(item, ":", item == decodedItem)
    print("File Print")
    with open(fileName, "r") as readFile:
        print(readFile.read())
    
#Dictionary
checker({"C# Tuning Fork": 19.99})
#list
checker([i for i in range(10)])
#tuple
checker((1,2,3))

#str
checker("C# Tuning Fork")

#int, long, float
checker(3)
checker(1234567890)
checker(3.14)

#boolean
checker(True)
checker(False)

#none
checker(None)


#Dictionary
checkerFile({"C# Tuning Fork": 19.99})
#list
checkerFile([i for i in range(10)])
#tuple
checkerFile((1,2,3))

#str
checkerFile("C# Tuning Fork")

#int, long, float
checkerFile(3)
checkerFile(1234567890)
checkerFile(3.14)

#boolean
checkerFile(True)
checkerFile(False)

#none
checkerFile(None)


