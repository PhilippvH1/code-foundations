#!/usr/bin/env python3

import cgi
import csv
form = cgi.FieldStorage()
color = form.getvalue('color')

with open('cgi-bin/col.csv', 'r') as colorscsv:
    readCSV = csv.reader(colorscsv, delimiter=',')
    for row in readCSV:
        if row[0] == color:
            html = f"""
                <html>
                  <head>
                    <title>COLORmatch</title>
                    </head>
                  <body style="background-color: {row[1]}">
                    <h1>{color} is a color.</h1>
                    <h2>{color} is a wonderful color.</h2>
                    <form action="/cgi-bin/color-checker.py" method="get" class="form-example">
                    <div class="form-example">
                        <label for="color">Enter a color: </label>
                        <input type="text" name="color" id="color" required>
                    </div>
                    <div class="form-example">
                        <input type="submit" value="Submit!">
                    </div>
                    </form>
                  </body>
                </html>
                """
            break

    else:
        html = """
        <html>
          <head>
            <title>NoCOLORmatch</title>
            </head>
          <body>
            <h1>THIS IS NOT A REAL COLOR YOU WEIRDO.</h1>
            <h2>So many options and you write {color}???</h2>
            <h3>I don't like it.</h3>
            <form action="/cgi-bin/color-checker.py" method="get" class="form-example">
            <div class="form-example">
                <label for="color">Enter a color: </label>
                <input type="text" name="color" id="color" required>
            </div>
            <div class="form-example">
                <input type="submit" value="Submit!">
            </div>
            </form>
          </body>
        </html>
        """

#print("Created HTML")
print (html)

#file = open("index.html","w+")
#file.write(html1)
#file.close()


#print("Motherf* HTML done")
