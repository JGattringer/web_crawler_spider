# importing functions get, post, time and Beautiful Soup
from requests import get, post
from bs4 import BeautifulSoup
import time
#importing the spider
from spider import Web_scrapy

response = get("https://pt.wikipedia.org/wiki/Ultima_Online")

# checking if the function get works
print(response)

# using the Beautiful Soup to map the content from the HTML
tags = BeautifulSoup(response.text, "html5lib")

#using tag to locate the title of the page
title = tags.find("title")
time.sleep(0.5)

print(f"Pagina Principal: {title.text}")

# get the links from secondary pages
links = tags.find_all("a", attrs={"class" : "mw-redirect"})
secondary_pages = [a.text for a in links]

pages = ["https://pt.wikipedia.org/wiki/Ultima_Online" + name for name in secondary_pages]

# loop to request all the links from the page, will use function sleep to have a cooldown between the request`s
for link in pages:
    PageRequest = get(link)
    Pg = BeautifulSoup(PageRequest.text, "html5lib").find('title')
    print(f'Pagina Secundaria: {Pg.text}')
    time.sleep(0.5)

