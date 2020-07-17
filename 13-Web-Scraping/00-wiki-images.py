import bs4
import re
import requests

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Grab all images on this page.
s_images = soup.select('img.thumbimage')
print('Number of thumb images: {}'.format(len(s_images)))
print(s_images[0])

print(type(s_images[0]))
computer_src = s_images[0]['src']
print(computer_src)

# Download an image and save to disk.
def download_to_disk(uri, protocol='https'):
    full_url = protocol + ':' + uri
    r_img = requests.get(full_url)
    re_filename = re.search('[^/]*$', uri)
    f = open(re_filename.group(0), 'wb')
    f.write(r_img.content)
    f.close()


# Download all images from article.
for s_image in s_images:
    download_to_disk(s_image['src'])
