'''
Project Name: Tarantula - The Web Crawler
File Name: domain.py
Author: Pratik Ashok Paranjape
Date: 05/23/2020
Project Description:
This a project to demonstrate the use of standard python libraries like os, urllib, HTMLParser
to create a minimalist webpage crawler that crawls webpages on a website to gather hyperlinks (URLs)
File Description:
This file acts as a helper by providing functions to get the domain name and sub-domain name
Credits:
Bucky Roberts | thenewboston
Youtube: https://www.youtube.com/playlist?list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0q
'''
'''
====================================================================================================
'''

# Import the urlparse class from urllib library
from urllib.parse import urlparse

# Get domain name (example.com)
def get_domain_name(url):
    # Enclosing in try-except block to check for any runtime-exceptions
    try:
        # Read from URL and get the sub domains from it
        results = get_sub_domain_name(url).split('.')
        # -2 is the actual domain name, without the top-level domain e.g. 'test' in www.test.com
        # -1 is the top-level domain e.g. 'com' in www.test.com
        # We return the domain name as below to get 'test.com' from 'www.test.com'
        return results[-2] + '.' + results[-1]
    # Try to catch exception
    except:
        # Do nothing if exception occurs
        return ''

# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    # Try getting the subdomain from URL e.g. 'www' from www.test.com
    try:
        # Return the subdomain name for parsing functions
        return urlparse(url).netloc
    # Catch exception
    except:
        # Do nothing
        return ''

'''
====================================================================================================
'''