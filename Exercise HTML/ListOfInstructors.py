from html.parser import HTMLParser
import urllib.request as Request

class MyHTMLParser(HTMLParser):
   lsClassNumbers = list()
   instructorDict = dict()
   isStrong = False

   def handle_data(self, data):
      if self.isStrong:
         if data[-1] == ":" :
            pass #this is the fee:
         #This should be a class number
         elif data[4] in [str(i) for i in range(10)]:
            self.lsClassNumbers.append(data)
         elif " " in data: # This should be an instructor's name:
            if data in self.instructorDict.keys():
               self.instructorDict[data] +=1
            else:
               self.instructorDict[data] = 1
      
   def handle_starttag(self, startTag, attrs):
        if startTag == 'strong':
           self.isStrong = True
  
   def handle_endtag(self, endTag):
      if endTag == 'strong':
         self.isStrong = False
             
#creating an object of the overridden class
parser = MyHTMLParser()
#Opening website using urllib's request
html_page = Request.urlopen(
    "http://www.cetc.umsl.edu/catalog/sql.html")

#Feeding the content
parser.feed(str(html_page.read()))
classNumbers = sorted(parser.lsClassNumbers)
print(classNumbers)
print(parser.instructorDict)
