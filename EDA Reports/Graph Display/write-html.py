# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 12:20:05 2019

@author: maherp
"""
import webbrowser as wb

f = open('C:/Users/maherp/Documents/GitHub/LA-Frac-ML-Pilot/EDA Reports/Graph Display/helloworld.html', 'w')

message = """<html>
<head></head>
<body><p>Hello World, again!<br>
More writing.</p></body>
</html>"""

f.write(message)
f.close()

wb.open('C:/Users/maherp/Documents/GitHub/LA-Frac-ML-Pilot/EDA Reports/Graph Display/helloworld.html',
        new=2, autoraise=True)
