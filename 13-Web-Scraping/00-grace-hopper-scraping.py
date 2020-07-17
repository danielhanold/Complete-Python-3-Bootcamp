import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup)

toc_text = soup.select('.toctext')
# print(toc_text)

first_item = toc_text[0]

for item in toc_text:
    print(item.getText())