import bs4
import requests

# Using fictional website toscrape.com, more specifically books subdomain.
# Goal: Get title of every book with 2-star
#       rating for books.toscrape.com.

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')
products = soup.select('.product_pod')

# example = products[0]

# # Determine if the product is rated with two stars.
# two_star_rated = example.select('.star-rating.Three') == []

# # Get title by getting the second link in the product,
# # and then grab the book title.
# second_link = example.select('a')[1]
# print(second_link['title'])

two_star_titles = []
for n in range(1, 51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('.star-rating.Two')):
            book_title = book.select('a')[1]['title']
            print('.', end='', flush=True)
            two_star_titles.append(book_title)

# Sort the list.
two_star_titles.sort()

print('All Two-Star Titles:')
for title in two_star_titles:
    print(title)
