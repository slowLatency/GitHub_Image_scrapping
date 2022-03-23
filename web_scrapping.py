#web scraping project is nothing but we give the URL to our program and ask it to perform some action
#over that url, for e.g: we give the url of a profile and ask our program to give us the link to the
#image of that particular profile(that's what we'll build in this module)

#first you have to import "Requests" and "bs4" module everytime before doing web scrapping.
# bs4 'Beautiful Soup' is a Python library for pulling data out of HTML and XML files and also it will
# help parse the content got from requests module into HTML or XML.
#Requests is the HTTP library using which we can deal with HTTP traffic using Python.
#webbrowser python module Comes with Python and opens a browser to a specific page


import requests
import webbrowser as wb
from bs4 import BeautifulSoup as bs

#this github_user variable will be storing the value or the username of the user whose profile pic we are 
#trying to scrape

githubUser=input('Enter the UserName: ')

# There are always some steps that we need to do while performing web scrapping.
# STEP1: is that we send a request to the URL and if we get the response code 200 it means the request 
# was successfully made. So alongwith this 200 code we'll get the whole HTML code of the page at that URL
# and once we get the whole HTML page we can easily get all the data that we are looking for.
# the Var URL we'll have the exact url of the page since we need to make our prg dynamic we'll be concatinating
# the username along with the url

url='https://github.com/' + githubUser



#requests.get(url) will send the request to the URL specified.

r = requests.get(url)

# using the bs() we are trying to get the content recived as the response using r.content and then 
# we are converting that content to HTML code using 'html.parser'  and then we are saving all that HTML
# code in the soup variable.

soup = bs(r.content, 'html.parser')
# print(soup)

# using this find method we are asking our code to go through the HTML content and then find a tag with 
# a particualr class or attribute or something
#find_all returns a list of dictionaries
# the first parameter specifying which tag in our case it is img tag
# the second attribute being the additional attributes of the img tag to distinctly identify that HTML object
# this profile_img variable will be a list.


profile_img_url = soup.find('img', {'alt' : 'Avatar'})['src']

#Opening the Link in the webbrowser
print(profile_img_url)
wb.open(profile_img_url)



