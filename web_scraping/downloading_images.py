import requests
from bs4 import BeautifulSoup
import random
import os

## Declaring the path variable that contains URL
path = 'https://www.gettyimages.in/photos/indian-cricket-team?mediatype=photography&phrase=indian%20cricket%20team&sort=mostpopular'

## Creating response object and storing text 
r = requests.get(path).text

## BeautifulSoup object
soup = BeautifulSoup(r, 'lxml')

## Fetching the URL for images that is to be downloaded
main_div = soup.find('div', class_='search-content__gallery-assets')
img = main_div.select('.gallery-asset__thumb')

## Storing URLS in a text file
with open('imglinks.txt', 'w') as links:
    for i in img:
        links.write(i['src']+ '\n')

## Path to the text file that stored Image Urls
txt_path = r'imglinks.txt'

## Creating output folder 
os.mkdir('DownloadedImages')

## Downloading the images from the website and storing it in Output folder
with open(txt_path) as f:
    lines= f.readlines()
    for url in lines:
        # webbrowser.open(i)
        url = url.strip()
        fname = random.randint(1,1000)
        image = open('DownloadedImages\\' + str(fname) + '.jpg', 'wb' )
        r = requests.get(url)
        image.write(r.content)
        image.close()
        





def extention(exten):
    f_name, ext = os.path.splitext(exten)
    return f_name, ext
