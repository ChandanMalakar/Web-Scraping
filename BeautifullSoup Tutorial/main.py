# Step 0 : Install the requirements
# pip install requests
# pip install bs4
# pip install html5lib


import requests
from bs4 import BeautifulSoup

url = "https://openweathermap.org/"  # stores the website link which has to be scraped


# Step 1 : Get the HTML

r = requests.get(url) # this .get() method of requests module is used to get the website content
htmlContent = r.content  # converts the content to the html form
# print(htmlContent) prints the content requested in html format


# Step 2 : Parse the HTML

soup = BeautifulSoup(htmlContent, "html.parser")  #BeautifulSoup() function is used to parse the htmlContent using the 'html.parser'
# print(soup.prettify) using .prettify allows it to display content in a clean manner



# Step 3 : Tree traverse the HTML

# Commonly used types of objects:
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup


# # 4. Comment
# markup = "<p><!-- This is a comment --></p>"
# soup2 = BeautifulSoup(markup, features="html5lib") #this features method is used to prevent the warnings.
# print(soup2.p)
# print(type(soup2.p.string)) # Directly prints the string inside the tag
# exit()



# to get the tag like head, body, title of the html, the (.<tag-name>) function is used
title = soup.title
print(title)


# to get all the paras of the html file

# .find_all() method is used to find all the paragraphs, anchors, etc. in the html content file



# To find all the paragraphs in the html file

# paras = soup.find_all('p') #here the parameter passed are the paragraph-p, etc. tags
# print(paras)

# The .find() method only returns the first paragraph, anchor, etc. in the HTML page
print(soup.find('p'))

# The class parameter returns the class name of the any element in the html page.
print(soup.find('p')['class'])


# find all the elements with a particular class name
# print(soup.find_all("p", class_="smartbanner-text"))



# Get the text from the tags/soup (directly prints all the content inside the html element)

# print(soup.find('p').get_text())
# print(soup.get_text()) (This method is used to get text of the entire html page without any html tags)


# To find all the anchors in the html file
anchors = soup.find_all('a')#here the parameter passed are the anchor-a, etc. tags
# print(anchors)


all_links = set() # here set is used to avoid repetition of links from the html file

# To print all the links on a html page
for link in anchors:
    if(link.get('href') != "#"):
        linkText = link.get('href')
        all_links.add(link)
        # print(linkText)


banner_android = soup.find(id='banner_android')
# print(banner_android.contents)

# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
# for elem in banner_android.contents:
#     print(elem)

for item in banner_android.stripped_strings:
    print(item)