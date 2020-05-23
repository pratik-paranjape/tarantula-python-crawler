'''
Project Name: Tarantula - The Web Crawler
File Name: link_finder.py
Author: Pratik Ashok Paranjape
Date: 05/23/2020
Project Description:
This a project to demonstrate the use of standard python libraries like os, urllib, HTMLParser
to create a minimalist webpage crawler that crawls webpages on a website to gather hyperlinks (URLs)
File Description:
This file contains various supporting parsing functions using 'HTMLParser' and 'urllib'
python modules that we will be using for our website crawler
Credits:
Bucky Roberts | thenewboston
Youtube: https://www.youtube.com/playlist?list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0q
'''
'''
====================================================================================================
'''

# We import the 'HTMLParser' class, and 'parse' class from html and urllib python libraries
from html.parser import HTMLParser
from urllib import parse

# We create a new 'LinkFinder' class to perform all the parsing functions
# to find URLs (links) on a webpage
class LinkFinder(HTMLParser):

    # We define the initialization function to use the 'base_url' and 'page_url' for parsing URLs
    def __init__(self, base_url, page_url):
        super().__init__()
        # We assign the base_url for use during parsing
        self.base_url = base_url
        # We assign page_url to parse URLs
        self.page_url = page_url
        # We create a set() object to store the links to be later used for storing onto a file
        self.links = set()

    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):
        # We parse the html file and look for <a> tag so that we can use the 'href' attribute
        # to get the links
        if tag == 'a':
            # We iterate over all the attributes of the <a> tag
            # and look for (attribute, value) tuples
            for (attribute, value) in attrs:
                # Here we check if the attribute is href, and try to get its value
                if attribute == 'href':
                    # We parse the 'base_url' object and get the value of 'href' attribute
                    # We assign this value to the url variable
                    url = parse.urljoin(self.base_url, value)
                    # Then we add this url to the links set() object
                    # to be later used for storing onto a file
                    self.links.add(url)

    # A function that returns all the URLs present on a webpage
    # that we parsed using the handle_starttag() function as shown above
    def page_links(self):
        # Returning the links set() object which has all the unique URLs from a particular webpage
        return self.links

    # Function to handle any errors caused during parsing of a webpage
    def error(self, message):
        # We handle the error by printing the error message on terminal
        print("Error: " + message)

'''
====================================================================================================
'''