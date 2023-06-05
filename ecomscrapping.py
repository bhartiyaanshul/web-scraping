import requests
from bs4 import BeautifulSoup
import pandas as pd

proxies = {
  "http": "http://37.120.192.154",
  "https": "https://37.120.192.154",
}
data = {'title': [],'price': []}
url = "https://www.amazon.in/s?k=iphone&crid=1356E1Y6BP688&sprefix=iphone%2Caps%2C234&ref=nb_sb_noss_1"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get(url, headers=headers)
   
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

# spans = soup.find(class_ ="a-size-medium a-color-base a-text-normal")
spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select("span.a-price-whole")
for span in spans: 
    print(span.string)
    data["title"].append(span.string)
    
for price in prices:
    print(price.string)
    data["price"].append(price.string)
    if len(data["price"]) == len(data["title"]):
        break
# print(spans)

df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv", index= False)

