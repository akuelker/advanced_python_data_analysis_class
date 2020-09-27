from html.parser import HTMLParser
import urllib.request as Request

class MyHTMLParser(HTMLParser):
    lsAnchors = list()
    lsClasses = list()
    
    def handle_starttag(self, startTag, attrs):
        if startTag == 'a':
            if attrs[0][0] == 'href':
                self.lsAnchors.append(attrs[0][1])

        
#create object of overridden class
parser = MyHTMLParser()
html_page = Request.urlopen("http://www.cetc.umsl.edu/catalog/sql.html")

parser.feed(str(html_page.read()))
#print("I'm your list!", parser.lsAnchors)

lsWorking=[]
lsBroken=[]
for url in parser.lsAnchors:
    try:
        if url[0] == '/':
            url = 'http://www.cetc.umsl.edu' + url
        html_page = Request.urlopen(url)
        lsWorking.append(url)
        print("YAY!" , url)
    except:
        lsBroken.append(url)
        print("It's broken!!!!:  ", url)
        #print("Details!: ", e)