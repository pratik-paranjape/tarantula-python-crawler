'''
Project Name: Tarantula - The Web Crawler
File Name: main.py
Author: Pratik Ashok Paranjape
Date: 05/23/2020
Project Description:
This a project to demonstrate the use of standard python libraries like os, urllib, HTMLParser
to create a minimalist webpage crawler that crawls webpages on a website to gather hyperlinks (URLs)
File Description:
This is the main file that creates multiple threads and assigns jobs to these threads.
This file also is the starting point of the project's execution
Credits:
Bucky Roberts | thenewboston
Youtube: https://www.youtube.com/playlist?list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0q
'''
'''
====================================================================================================
'''

# Import threading from python standard libraries to implement multi-threading
import threading
# Import Queue from queue library to main job queues for workers
from queue import Queue
# Import Spider() class from spider custom library to perform crawling operations
from spider import Spider
# Import all functions from domain library, to perform domain name operations
from domain import *
# Import functions from general library, to perform
# standard parsing/crawling supporting operations
from general import *

# Global variable to store project name - Users change this value
PROJECT_NAME = 'SMA'
# Global variable to store homepage url - Users change this value
HOMEPAGE = 'https://sagarmusicacademy.com/'
# Global variable that extracts domain name from homepage url
DOMAIN_NAME = get_domain_name(HOMEPAGE)
# Queue file name
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
# Crawled file name
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
# Number of threads - Users can experiment to see performance changes
NUMBER_OF_THREADS = 8

# Create an empty Queue() object
queue = Queue()

# Initialize the Spider() class
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# Create worker threads (will die when main exits)
def create_workers():
    # Iterate over number of threads
    for _ in range(NUMBER_OF_THREADS):
        # Create a new worker (thread) and assign operation to perform as work()
        t = threading.Thread(target=work)
        # Keep the worker (thread) in daemon mode, so as to auto-kill the daemon when process exits
        t.daemon = True
        # Start the worker (thread)
        t.start()

# Do the next job in the queue
def work():
    # As long as work is not done
    while True:
        # Get the next URL to be parsed
        url = queue.get()
        # Crawl the webpage at that url
        Spider.crawl_page(threading.current_thread().name, url)
        # return when task is done
        queue.task_done()

# Each queued link is a new job
def create_jobs():
    # Iterate over all the links in queue file
    for link in file_to_set(QUEUE_FILE):
        # add new link to the queue
        queue.put(link)
    # Join the queue set() object
    queue.join()
    # Start crawling
    crawl()

# Check if there are items in the queue, if so crawl them
def crawl():
    # Get all the queued links from the queue file
    queued_links = file_to_set(QUEUE_FILE)
    # If there are links that have NOT been crawled
    if len(queued_links) > 0:
        # Print how many links are still there in the queue
        print(str(len(queued_links)) + ' links in the queue')
        # Start creating jobs for workers (threads) to crawl these pages
        create_jobs()

# First we create workers (threads)
create_workers()

# Then we ask the workers (threads) to start crawling webpages
crawl()

'''
====================================================================================================
'''