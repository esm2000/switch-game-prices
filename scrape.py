import requests
from bs4 import BeautifulSoup as soup 
import numpy as np 
import pandas as pd 

# arrays that will hold each page's html content 
page_htmls = []

# arrays that will hold the data 
names, links, prices, ratings, conditions, sell_infos = [], [], [], [], [], []

# grab html 
# for i in range(1, 11):
i = 1
print('page %d...' % i)
url_base = 'https://www.ebay.com/sch/i.html?_dcat=139973&_sop=12&LH_TitleDesc=0&_fsrp=1&_sacat=139973&_nkw=switch&_from=R40&Region%2520Code=NTSC%252DU%252FC%2520%2528US%252FCanada%2529&Platform=Nintendo%2520Switch&LH_PrefLoc=1&rt=nc&_pgn='
url = url_base + str(i)
req = requests.get(url)
page_html = req.text
page_htmls.append(page_html)

# parse the html 
# for page_html in page_htmls:
page_soup = soup(page_html, 'html.parser')

# find all item containers
containers = page_soup.findAll('div', {'class': 's-item__info clearfix'})

for container in containers:

    # extract all info 
    name = container.find('h3', {'class': 's-item__title'}).string
    link = container.find('a')['href']
    price = container.find('span', {'class': 's-item__price'}).string

    rating_container = container.find('div', {'class': 'x-star-rating'})
    if rating_container is not None:
        rating = rating_container.find('span', {'class':'clipped'}).string
    else: 
        rating = None

    condition = container.find('span', {'class': 'SECONDARY_INFO'}).string

    sell_info = container.find('span', {'class': 'BOLD NEGATIVE'})
    if sell_info is not None:
        sell_info = sell_info.string
    else:
        sell_info = None 

    # put info into arrays
    names.append(name)
    links.append(link)
    prices.append(price)
    ratings.append(rating)
    conditions.append(condition)
    sell_infos.append(sell_info)

for i in range(10):
    print(names[i])
    print(links[i])
    print(prices[i])
    print(ratings[i])
    print(conditions[i])
    print(sell_infos[i])

print(len(names))