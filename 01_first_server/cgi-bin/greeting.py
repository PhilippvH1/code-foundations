#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage() 

name = form.getvalue('superheroname')
mail  = form.getvalue('superheroemail')

print(name)

html1 = f"""
<html>
  <head>
    <title>pythonPage</title>
    </head>
  <body>
    <h1>Ihr seid alle {name}.</h1> 
    <h2>Wir sind alle {mail}.</h2> 
    <h3>Ich nicht.</h3>
  </body> 
</html>
"""


#print("Created HTML")
print (html1)

#file = open("index.html","w+")
#file.write(html1) 
#file.close() 


#print("Motherf* HTML done")