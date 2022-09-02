import sys
import bs4
import webbrowser
import requests

def getPara():
    para = sys.argv[1:]
    return para[0]

def openWebBro(keyword:str):
    url = f'https://www.google.com/search?q={keyword}'
    webbrowser.open(url)


resp = requests.get(f'https://www.google.com/search?q={getPara()}')
print(resp.text)