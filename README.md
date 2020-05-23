# Tarantula - A python based website crawler!
This a project to demonstrate the use of standard python libraries like os, urllib, HTMLParser to create a minimalist webpage crawler that crawls webpages on a website to gather hyperlinks (URLs)

## Files in Project:
- general.py<br />
- link_finder.py<br />
- domain.py<br />
- spider.py<br />
- main.py

## How to run:
**Step 1: Make the necessary changes**<br />
Navigate to file `main.py` and change the following lines<br />
- To create a new project<br />
`PROJECT_NAME = 'TEST'`<br />
Change the project name from `TEST` to `YOUR_PROJECT_NAME`<br />
- To add the homepage URL<br />
`HOMEPAGE = 'https://example.com/'`<br />
Change the link from `https://example.com/` to `TARGET_WEBSITE_HOMEPAGE_LINK` {make sure to use the format as http(s)://abc.xyz}<br />
- To change number of workers (Threads)<br />
Change this variable `NUMBER_OF_THREADS = 8` to `YOUR_THREADS` {Default is 8}<br />

**Step 2: Run the crawler**
- Using Python 2:<br />
`python main.py`
- Using Python 3:<br />
`python3 main.py`

## File Descriptions:

#### 1. general.py - [url](./general.py)
This file contains various supporting functions that we will be using for our website crawler

#### 2. link_finder.py - [url](./link_finder.py)
This file contains various supporting parsing functions using 'HTMLParser' and 'urllib' python modules that we will be using for our website crawler

#### 3. domain.py - [url](./domain.py)
This file acts as a helper by providing functions to get the domain name and sub-domain name

#### 4. spider.py - [url](./spider.py)
The actual Spider class that performs all the webpage crawling functions

#### 5. main.py - [url](./main.py)
This is the main file that creates multiple threads and assigns jobs to these threads. This file also is the starting point of the project's execution
