from html.parser import HTMLParser
import urllib.request as Request

class MyHTMLParser(HTMLParser):
   lsAnchors = list()

   def handle_starttag(self, startTag, attrs):
        if startTag == 'a':
            if attrs[0][0] =='href':
               self.lsAnchors.append(attrs[0][1])
             
#creating an object of the overridden class
parser = MyHTMLParser()
#Opening website using urllib's request
html_page = Request.urlopen(
    "http://www.cetc.umsl.edu/catalog/sql.html")

#Feeding the content
parser.feed(str(html_page.read()))
lsWorking = []
lsBroken = []
for url in parser.lsAnchors:
    try:
        #print("anchors", parser.lsAnchors)
        if url[0] == '/':
            url = "http://www.cetc.umsl.edu" + url
        html_page = Request.urlopen(url)
        lsWorking.append(url)
    except ValueError as e:
        lsBroken.append(url)
        print("URL has issues: ", url)
        print("Problem details:", e)
    except (e):
        print("Another error", e)
print("Broken links:", lsBroken)
print("Working links:", lsWorking)

