# How to scrape a Page from a site and Saving Scraped Data to CSV

import urllib.request
import bs4
import csv

# Downloading
url = 'https://news.ycombinator.com/'
data = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(data, "html.parser")

# Extracting
links = soup.select("a.storylink")

# Saving
with open('articles.csv','w') as tsvfile:
	writer = csv.writer(tsvfile, delimiter="\t")
	writer.writerow( ('Link', 'Title') )
	for link in links:
		writer.writerow( (link['href'], link.txt) )
	#print(f"{link['href']} {link.text}")