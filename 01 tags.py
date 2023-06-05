import requests
from bs4 import BeautifulSoup

with open("times.html","r") as f:
    html_doc = f.read()
   
   
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.title.string)
# print(soup.div)
# print(soup.find_all("div"))
# print(soup.get_text())
for child in soup.find(id= "navbar").children:
    print(child)