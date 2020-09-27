from html.parser import HTMLParser
import urllib.request as Request

class MyHTMLParser(HTMLParser):
    isStrong = False
    lsClassIDs = list()
    def handle_data(self, data):
      if self.isStrong:
         if data[-1] == ":" :
            pass #this is the fee:
         #This should be a class number
         elif data[4] in [str(i) for i in range(10)]:
            self.lsClassIDs.append(data)
      
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
lsClassIDs = sorted(parser.lsClassIDs)
print(lsClassIDs)
print('Number of classes taught on this page: ', len(lsClassIDs))

