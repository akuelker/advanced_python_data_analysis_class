import xml.etree.ElementTree as et
import xml.dom.minidom as mindom

def printNiceXML(elem):
    roughString = et.tostring(elem, 'utf-8')
    reparsed = mindom.parseString(roughString)
    return reparsed.toprettyxml(indent = "  ")
