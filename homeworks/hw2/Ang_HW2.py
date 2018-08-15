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

address='https://petitions.whitehouse.gov/?page='+str(page-1) #get address from " next to last page," which is the last page with petitions
web_page = urllib2.urlopen(address)
soup = BeautifulSoup(web_page.read()) #
#-----------------------------------------------------------------------

with open('Ang_HW2.csv', 'wb') as f:
	#-------------------------------------------------------------------------
	# make skeleton of csv
	#-------------------------------------------------------------------------
	w = csv.DictWriter(f, fieldnames = ("title", "publishdate", "issues", "signatures"))
	w.writeheader()
	petitions={}#create an empty dictionary
 	

	#-------------------------------------------------------------------------
	# Get titles from https://petitions.whitehouse.gov/petitions
	#-------------------------------------------------------------------------
	#<a href="/petition/do-not-repeal-net-neutrality">Do Not Repeal Net Neutrality</a>
	pet_soup.find_all('a').attrs['href']

	#-------------------------------------------------------------------------
	#get Issues from https://petitions.whitehouse.gov/petitions
	#-------------------------------------------------------------------------
	#<span class="signatures-number">275,457</span>
	
	petitions['signatures']=[i.get_text().encode('utf-8') for i in pet_soup.find_all('span', {'class':"signatures-number"})]
	###remove comma and covert to integer

	#-------------------------------------------------------------------------
	#get number of signatures from https://petitions.whitehouse.gov/petitions
	#-------------------------------------------------------------------------
	#<div class="signatures-text-container"><span class="signatures-number">275,457</span>
	<span class="signatures-text">signed</span>
	</div>
	#get publish date from individual petition pages



#-------------------------------------------------------------------------
#write csv
#-------------------------------------------------------------------------
import csv