# HOMEWORK
# Go to https://petitions.whitehouse.gov/petitions
# Go to the petition page for each of the petitions.
# Create a .csv le with the following information for each petition:
# 	Title
# 	Published date
# 	Issues
# 	Number of signatures
from bs4 import BeautifulSoup
import urllib2 

address= 'https://petitions.whitehouse.gov/petitions'
web_page=urllib2.urlopen(address)

pet_soup= BeautifulSoup(web_page.read())