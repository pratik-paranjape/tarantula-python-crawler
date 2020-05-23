'''
Project Name: Tarantula - The Web Crawler
File Name: spider.py
Author: Pratik Ashok Paranjape
Date: 05/23/2020
Project Description:
This a project to demonstrate the use of standard python libraries like os, urllib, HTMLParser
to create a minimalist webpage crawler that crawls webpages on a website to gather hyperlinks (URLs)
File Description:
The actual Spider class that performs all the webpage crawling functions
Credits:
Bucky Roberts | thenewboston
Youtube: https://www.youtube.com/playlist?list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0q
'''
'''
====================================================================================================
'''
# Importing 'urlopen' class from 'urllib' python library to make connection to webpages
# and get response
from urllib.request import urlopen
# Importing the 'LinkFinder' class from the custom link_finder library
# that we created for parsing webpages and finding links on them
from link_finder import LinkFinder
# We import all functions from the domain library to perform domain name operations
from domain import *
# We import all functions from general library (general.py) that we created
# for various crawl functionalities
from general import *

# We create a 'Spider' class, which we will be using to create objects
# which will do webpage crawling for us
class Spider:

    # variable to hold project name,
    # which will be used to create directory
    project_name = ''
    # variable to hold base URL,
    # which will be used to start parsing of webpage
    base_url = ''
    # variable to hold domain name,
    # which will be used for domain operations
    domain_name = ''
    # variable to hold queue file name,
    # which will be used to store the list of queued URLs
    queue_file = ''
    # variable to hold crawled file name,
    # which will be used to store the list of crawled URLs
    crawled_file = ''
    # variable to hold queue set() object,
    # which will be used for storing list of unique URLs to be queued
    queue = set()
    # variable to hold crawled set() object,
    # which will be used for storing list of unique URLs to be crawled
    crawled = set()

    # Initialization function to initialize the values of global variables
    def __init__(self, project_name, base_url, domain_name):
        # Set up project name
        Spider.project_name = project_name
        # Set up project's base URL
        Spider.base_url = base_url
        # Set up project's domain name
        Spider.domain_name = domain_name
        # Create queue.txt for the project
        Spider.queue_file = Spider.project_name + '/queue.txt'
        # Create crawled.txt for the project
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        # Boot function call to start some important set-up related operations
        self.boot()
        # Page crawl function
        self.crawl_page('First spider', Spider.base_url)

    # Creates directory and files for project on first run and starts the spider
    @staticmethod
    def boot():
        # Creates project directory by project name
        create_project_dir(Spider.project_name)
        # Creates queue.txt and crawled.txt files for the project
        create_data_files(Spider.project_name, Spider.base_url)
        # creates a set() object from queue.txt file
        Spider.queue = file_to_set(Spider.queue_file)
        # creates a set() object from crawled.txt file
        Spider.crawled = file_to_set(Spider.crawled_file)

    # Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(thread_name, page_url):
        # Check if the files have NOT been crawled yet
        if page_url not in Spider.crawled:
            # Print which thread is crawling which page URL
            print(thread_name + ' now crawling ' + page_url)
            # Print queue and crawled set() objects's lengths
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled  ' + str(len(Spider.crawled)))
            # Keep adding new links to queue
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            # Once crawled, remove from queue set() object
            Spider.queue.remove(page_url)
            # Once crawled, add to crawled set() object
            Spider.crawled.add(page_url)
            # Update queue.txt and crawled.txt files
            Spider.update_files()

    # Converts raw response data into readable information and checks for proper html formatting
    @staticmethod
    def gather_links(page_url):
        # Create a variable/object to store HTML request's response
        html_string = ''
        # Enclose in a try-except block to handle exceptions during connections
        try:
            # Get the response after trying to connect to a webpage
            response = urlopen(page_url)
            # Check if response contains, text/html as Content-Type in header
            if 'text/html' in response.getheader('Content-Type'):
                # Read the response byte wise
                html_bytes = response.read()
                # Decode the response from byte order to human readable format
                # And store in variable/object created earlier to store response
                html_string = html_bytes.decode('utf-8')
            # Create a LinkFinder() object to start parsing webpages
            finder = LinkFinder(Spider.base_url, page_url)
            # Start parsing webpages using HTMLParser class's feed function
            finder.feed(html_string)
        # Catch exception
        except Exception as e:
            # Print exception info to console
            print(str(e))
            # Since exception occured, return empty set() object
            return set()
        # If all operations are successful, return results
        return finder.page_links()

    # Function to add links to queue
    @staticmethod
    def add_links_to_queue(links):
        # Iterate over every URL in links set() object
        for url in links:
            # Check if URL is present in queue or crawled set(), continue without adding
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            # Check if URL is same as domain name, if yes, continue without adding
            if Spider.domain_name != get_domain_name(url):
                continue
            # If all the above checks fail, proceed to add the URL to queue set() object
            Spider.queue.add(url)

    # Function to update queue.txt and crawled.txt files
    @staticmethod
    def update_files():
        # Function to write data from queue set() object to queue.txt
        set_to_file(Spider.queue, Spider.queue_file)
        # Function to write data from crawled set() object to crawled.txt
        set_to_file(Spider.crawled, Spider.crawled_file)

'''
====================================================================================================
'''