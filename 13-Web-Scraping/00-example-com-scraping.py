import requests
import bs4

result = requests.get("http://www.example.com")

print(type(result))

# print(result.text)

# Create BS object
soup = bs4.BeautifulSoup(result.text, 'lxml')

print(soup)

# use getText() to get text without tag
# for a BS text object
title_tag = soup.select('title')[0].getText()
print(title_tag)

p_tags = soup.select('p')
print(p_tags[0].getText())

