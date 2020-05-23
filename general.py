'''
Project Name: Tarantula - The Web Crawler
File Name: general.py
Author: Pratik Ashok Paranjape
Date: 05/23/2020
Project Description:
This a project to demonstrate the use of standard python libraries like os, urllib, HTMLParser
to create a minimalist webpage crawler that crawls webpages on a website to gather hyperlinks (URLs)
File Description:
This file contains various supporting functions that we will be using for our website crawler
Credits:
Bucky Roberts | thenewboston
Youtube: https://www.youtube.com/playlist?list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0q
'''
'''
====================================================================================================
'''

# Importing the os python module to use in-built functions for creating directories/files
import os

# Creating a separate folder for each website - a simulation of Workspaces
def create_project_dir(directory):
    # Here we check if the said directory/workspace/project already exists,
    # if not then we create a new directory/workspace/project
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)

# Creating two files to keep track of URLs that are queued and URLs that have already been crawled
def create_data_files(project_name, base_url):
    # Here we specify that the file queue.txt and crawled.txt should
    # be created inside our directory/workspace/project
    queue = os.path.join(project_name , 'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')
    # Here we check if the said files already exists,
    # if not then we create the new files
    if not os.path.isfile(queue):
        # We write/copy the base_url (top-level domain name) into our queue.txt file
        # as this is the first web page that we need to crawl for web links
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        # Intutively the crawled.txt file should be empty
        # as during the first run it will not have crawled any of the web pages
        write_file(crawled, '')

# Function to write data to a file
def write_file(path, data):
    # We first open the file specified in the "path" variable in write mode,
    # hence the 'w' attribute in the open() system call
    with open(path, 'w') as f:
        # Then we write the data from the data variable
        # to the file opened in write mode
        f.write(data)

# Function to append data to an existing file
def append_to_file(path, data):
    # We first open the file specified in the 'path' variable in append mode,
    # hence the 'a' attribute in the open() system call
    # This allows us to append (add at the end of file) data to a file
    with open(path, 'a') as file:
        # Then we start writing the data (in this case URLs) to the file,
        # and use a '\n' to automatically send the cursor to the next line
        file.write(data + '\n')

# Function to delete contents of a file
def delete_file_contents(path):
    # We open the file in write mode by specifying the 'w' attribute in the open() system call
    # And we close the file without writing any data to the file,
    # hence deleting all the previous content as we did not open the file in append mode
    open(path, 'w').close()

# Here we try to convert the list of URLs from a file into a set() object,
# so that there are no repitions during crawling function
# and every element of the set() object being unique
def file_to_set(file_name):
    # We first create an empty set() object
    results = set()
    #Then we open a file in read-text 'rt' mode using the open() system call
    with open(file_name, 'rt') as f:
        # We iterate over all the lines in the file
        for line in f:
            # Then append every unique line to the set() object
            results.add(line.replace('\n', ''))
    # Then we return the updated set() object to be used for further processing
    return results

# Here we try to convert a set() object containing unique URLs to a file,
# so that there are no repitions during crawling function
# and we can use the file for storing data
def set_to_file(links, file_name):
    # We open the file in write mode by specifying 'w' attribute in the open() system call
    with open(file_name,'w') as f:
        # Then we iterate over all the links from the set() object
        # in a sorted manner so that we have alphabetically sorted list
        for l in sorted(links):
            # And we write these unique elements of the set() object to the file
            f.write(l+'\n')

'''
====================================================================================================
'''