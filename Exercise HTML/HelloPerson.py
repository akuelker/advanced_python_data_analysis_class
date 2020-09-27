import webbrowser
fileName = 'helloworld.html'

userName = input("Enter your name")
startHtmlText = """<html>
<head>Hello"""
endHtmlText = """</head>
<body><h1>Hello World</h1>
<p>Nice Day, isn't it?</p></body>
</html>"""

with open(fileName,'w') as webFile:
    webFile.write(startHtmlText + " " + userName + endHtmlText)

#Change path to reflect file location
webbrowser.open_new_tab(fileName)
