'''
Created on 24-Sep-2015

@author: sumit
'''
import urllib
import lxml.html
from lxml import html
import requests

print("Please enter the wikipedia URL and press Enter key.....")

inputURL = raw_input() # take URL input from the user and store it into 'inputURL'

#open the input URL with urllib module of python
connection = urllib.urlopen(inputURL)

#parse HTML from the webpage using lxml module of Python
dom =  lxml.html.fromstring(connection.read())

titleOfLinks = [] #stores the list of title of links to the pages found on the page

backLinks = [0, 0] #stores the count of link with maximum backlinks and its corresponding Page Title

backLink_count = 0 #initialize backlink count to 0

for link in dom.xpath('//a/@title'): # select the "title" for all "a tags"(links)
    titleOfLinks.append(link) #append it to the list of title of links found on that page
    
print ("No of links found on this page is --> %s" % len(titleOfLinks)) #prints the total no of title of links found on the user provided wikipedia link  
print ("")
print ("The tiles/page name for all the links are --> ") 
print (titleOfLinks) #print all the "titles" of the links to their respective pages.
print ("")
print ("")
#iterate through the list of "titles" and check their "backlink counts" from the backlink counter provided by wikipedia
#URL to check the backlink count is--> "http://dispenser.homenet.org/~dispenser/cgi-bin/backlinkscount.py?title=Page_name"  
for title in titleOfLinks:
    backlink_found = requests.get('http://dispenser.homenet.org/~dispenser/cgi-bin/backlinkscount.py?title=%s' %title)    
    backlink_parsed_into_text = html.fromstring(backlink_found.text)
    into_text = int(backlink_parsed_into_text.text)
    if into_text > backLink_count: 
        backLink_count = into_text  #update the "backLink_count" variable
        backLinks = [backLink_count, title] #store the updated count with its respective Page Name/title in the list

#finally append the page name/title with max backlinks to the default wikipedia URL to get the desired result.        
res_URL = 'https://en.wikipedia.org/wiki/'+backLinks[1]

print ("The Most popular link in this page is--> ")
#print the resulting URL
print (res_URL)
