
# coding: utf-8

# In[1]:


import xml.etree.ElementTree as et
from xml.dom import minidom


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = et.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

top = et.Element('top')

comment = et.Comment('Generated for PyMOTW')
top.append(comment)

child = et.SubElement(top, 'child')
child.text = 'This child contains text.'

child_with_tail = et.SubElement(top, 'child_with_tail')
child_with_tail.text = 'This child has text.'
child_with_tail.tail = 'And "tail" text.'

child_with_entity_ref = et.SubElement(top, 'child_with_entity_ref')
child_with_entity_ref.text = 'This & that'

#print(et.tostring(top))
print(prettify(top))



# In[ ]:



