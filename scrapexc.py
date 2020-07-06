# Write a Python program that uses BeautifulSoup to go to https://news.google.com 
# and prints out all of the headlines on the page. 

import urllib.request
from bs4 import BeautifulSoup

url = 'https://news.google.com'
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, "html.parser")

titles = soup.select(".titletext")

headlines = [title.text for title in titles]

def find_headline_by_keyword(hlines, kwds):
	return print([headline for headline in hlines if kwds.lower() in headline.lower()])

print(find_headline_by_keyword(headlines, "covid19")	)