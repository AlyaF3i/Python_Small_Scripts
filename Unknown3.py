"""
import bs4
import requests
import urllib
import numpy as np
f=open('html.html','w')
#file=urllib.request.urlopen( r'https://www.mohap.gov.ae/en/AwarenessCenter/Pages/COVID19-Information-Center.aspx')
file=requests.get(r'https://www.mohap.gov.ae/en/AwarenessCenter/Pages/COVID19-Information-Center.aspx',verify=False)
f.write(file.text.encode(encoding="utf-8"))
f.open('',encode='utf-8')
exampleSoup = bs4.BeautifulSoup(file.text.encode(encoding="utf-8"), 'html.parser')
numbers=exampleSoup.select('.numbers')
dates=exampleSoup.select('.date')
dates = [a.getText() for a in dates][::-1]
CasesPerDay = [int(a.getText()) for a in numbers][::-1]
print(dates)
xAxis=np.array([0,len(CasesPerDay)-1])
Text= "From 4, Feb, 2021  To  14 May"
print(numbers)
"""
import 
a=str("hello").count("hello")
