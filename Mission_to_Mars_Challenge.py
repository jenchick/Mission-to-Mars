#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import Splinter and BeautifulSoup

from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[3]:


# set your executable path in the next cell, then set up the URL (NASA Mars News (Links to an external site.)) for scraping.

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[23]:


# assign the url and instruct the browser to visit it

# Visit the mars nasa news site

url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[24]:


# set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[25]:


# begin scraping

slide_elem.find('div', class_='content_title')


# In[26]:


# we need to get just the text, and the extra HTML stuff isn't necessary
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[8]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[27]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[28]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[29]:


img_soup = soup(html, 'html.parser')


# In[30]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[31]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[33]:


# Module 10.3.5 Scraping entire table with Pandas
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[34]:


# Convert the df back into HTML-ready code
df.to_html()


# In[35]:


# End the automated  browsing session; important or else you will use up all the ccomputer's resources
browser.quit()


# In[25]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[26]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[11]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[13]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[14]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[15]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[27]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[32]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Parse the resulting html with soup


#for XXX in XXX
# a.) Click on each hemisphere link
# b.) navigate to the full-resolution image (will have .jpg extension)
# c.) retrieve the full-resolution image URL string and title for the hemisphere image
#     (click the link, find the "sample" image anchor tag, and get the "href")
#     save the full-resolution image string as the value for the "img_url" key that will be stored in the dict you created
#     in hint
#     save the hemisphere image title as the value for the "title" key that will be stored in the dict you created in hint
#     before getting next image URL & title, add the dict with image URL string and hemisphere title to the list created in #2
# d.) use "browser.back()" to navigate back to the beginning to get the next hemisphere image


# Copied this portion of code with Nick Foley's permission during Office Hours on 6/25/2022 
#after he walked through it for me to help me understand the process.

for i in range(4):
    # Create empty dict
        hemispheres = {}
        # Click button to go to link for picture
        browser.find_by_css('a.product-item img')[i].click()
        # Find URL location
        element = browser.links.find_by_text('Sample').first
        # Pull image
        img_url = element['href']
        # Pull title
        title = browser.find_by_css('h2.title').text
        # Add img_url to dict
        hemispheres['img_url'] = img_url
        # Add hemispehere title to dict
        hemispheres['title'] = title
        # Add hemispheres dict to  hemispheres_image_urls list
        hemisphere_image_urls.append(hemispheres)
        browser.back()


# In[33]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[34]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:




