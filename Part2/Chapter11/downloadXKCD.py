import bs4,requests,os

url = "https://xkcd.com/2662/"

resp = requests.get(url)
respT = resp.text
# print(respT)
resp.close()

respSoup = bs4.BeautifulSoup(respT)
target = respSoup.select('#comic > a > img')

comicUrl = 'https:' + target[0].get('src')

print(comicUrl)