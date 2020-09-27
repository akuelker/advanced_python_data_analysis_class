import webbrowser
fileName = 'helloWorld.html'
htmlText = '''
<html>
<head>Hello World</head>
<body><h1>Peekaboo</h1>
<p>I'm a little paragraph</p>
</body>
</html>
'''
with open(fileName, 'w') as webFile:
    webFile.write(htmlText)
webFile.close()    
webbrowser.open_new_tab(fileName)