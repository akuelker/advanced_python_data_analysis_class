import webbrowser
fileName = 'helloworld.html'

htmlText = """<html>
<head>Hello</head>
<body><h1>Hello World</h1>
<p>Nice Day, isn't it?</p></body>
</html>"""

with open(fileName,'w') as webFile:
    webFile.write(htmlText)

#Change path to reflect file location
webbrowser.open_new_tab(fileName)
