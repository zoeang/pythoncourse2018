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
import csv
#-------------------------------------------------------------------------
# Get soup for all webpages
# Write while loop to get the soup for the page with all of the petitions.
# The loop will break when there is a page that does not have petitions. 
#-------------------------------------------------------------------------

page=0 #initiate iterator
petitions_on_page=True #test condition
while petitions_on_page:
	address='https://petitions.whitehouse.gov/?page='+str(page) #get address
	web_page = urllib2.urlopen(address)
	soup = BeautifulSoup(web_page.read())
	soup.find_all('div', {'class':'view-content'}) #this class does not exist if there are not petitions a=on a page
	if len(soup.find_all('div', {'class':'view-content'}))==0: #condition is true for a page without petitions
		break 
		#petitions_on_page=False
		#return page
	page+=1 #add 1 to iterator if there was not a break
list_of_soups=[]
for i in range(0, page):
	address='https://petitions.whitehouse.gov/?page='+str(i) #get address from " next to last page," which is the last page with petitions
	web_page = urllib2.urlopen(address)
	soup = BeautifulSoup(web_page.read()) #
	list_of_soups.append(soup)
#-----------------------------------------------------------------------

with open('Ang_HW2.csv', 'wb') as f:
	#-------------------------------------------------------------------------
	# make skeleton of csv
	#-------------------------------------------------------------------------
	w = csv.DictWriter(f, fieldnames = ("title", "publishdate", "issues", "signatures"))
	w.writeheader()
	petitions={} #create an empty dictionary
	#-------------------------------------------------------------------------
	# Get webpage for each petition
	#-------------------------------------------------------------------------
	all_petitions=[] #list of all url extensions
	for soup in list_of_soups: #each element in list_of_soups is a webpage; there are 4 elements
		list_of_h3=soup.find_all('h3')
		for i in list_of_h3:
			try:
				all_petitions.append('https://petitions.whitehouse.gov'+i.a.attrs["href"].encode('utf-8'))
			except:
				pass
	#-------------------------------------------------------------------------
	# Fill in data
	#-------------------------------------------------------------------------	
	for i in all_petitions:
		#make soup for each webpage
		web_page = urllib2.urlopen(i)
		page_soup = BeautifulSoup(web_page.read())
		#-------------------------------------------------------------------------
		# Titles
		#-------------------------------------------------------------------------
		#<a href="/petition/do-not-repeal-net-neutrality">Do Not Repeal Net Neutrality</a>
		title=page_soup.find('h1', {'class': 'title'})
		petitions['title']=title.get_text().encode('utf-8')
		#-------------------------------------------------------------------------
		# Publish Date
		#-------------------------------------------------------------------------
		petitions['publishdate']=str(page_soup.find('h4', {'class': 'petition-attribution'})).split(' on ')[1][:-5]
		#-------------------------------------------------------------------------
		# Issues
		#-------------------------------------------------------------------------
		issues=page_soup.find('div', {'class': 'field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags'}).find_all('h6')
		petitions['issues']=[i.get_text().encode('utf-8') for i in issues] #why won't this work like line 68? mult elements?
		#-------------------------------------------------------------------------
		# Signatures
		#-------------------------------------------------------------------------
		petitions['signatures']=page_soup.find('span', {'class':"signatures-number"}).get_text()
		#-------------------------------------------------------------------------
		# Write Observation to row of csv
		#-------------------------------------------------------------------------
		w.writerow(petitions)

