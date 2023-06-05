import requests

def fetchandsavedata(url,path):
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)
    
url = "https://www.amazon.in/"

fetchandsavedata(url,"data/times.html")