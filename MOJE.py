import requests
from bs4 import BeautifulSoup
import re
import openpyxl 
from openpyxl import Workbook
 
r = requests.get('https://wiki.lineageos.org/devices/#xiaomi')
 
soup = BeautifulSoup(r.content, 'html.parser')

smazat = soup.find_all(class_="item discontinued hidden")
for smaz in smazat:
    smaz.decompose()

path = "gfg.xlsx"

items = soup.find_all(class_="item")

workbook = Workbook()
sheet = workbook.active

for count,item in enumerate(items):
    sheet["A{}".format(count+1)] = count
    sheet["B{}".format(count+1)] = item.find(class_="devicename").text
    sheet["C{}".format(count+1)] = item.find(class_="codename").text

workbook.save(path)