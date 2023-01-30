# if you want to scrape a website 
#     1. Use the API
#     2. HTML Web Scraping using some tool like bs4



# Step 0: Install all the requirements
# !pip install requests
# !pip install bs4
# !pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "http://codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlcontent = r.content
# print(htmlcontent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify())

# Step 3: HTML Tree Traversal
# soup is like a tree

# commonly used types of objects
#     1. Tag
#     2. Navigable String
#     3. BeautifulSoup
#     4. Comment
# markup = "<p><!-- This is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string)) # comment object (explore yourself)
# exit()

# get the title of the HTML page
title = soup.title
# print(title)

# print(type(soup)) # BeautifulSoup object
# print(type(title)) # Tag object
# print(type(title.string)) # NavigableString

# get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)

# get all the anchor tags from the page
anchors = soup.find_all('a')
# print(anchors)

# get first element in the html page
# print(soup.find('p'))

# get classes of any element in the html page
# print(soup.find('p')['class'])
# you can also get 'id' of elements in the html page but be careful as it does not exist in many of the pages

# find all the elements with class lead
# print(soup.find_all("p",class_="text-sm"))

# get the text from the tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())

# Get all the links on the page
all_links = set()
for link in anchors:
    if "https" not in link.get('href'):
        link = "http://codewithharry.com"+link.get('href')
    else:
        link = link.get('href')
    all_links.add(link)

for link in all_links:
    print(link)

# .parent .parents .children .content
# parents and children are generator they will eat less memory