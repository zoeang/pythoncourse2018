
import imp
import os


meetup = imp.load_source('labexercises', 'meetupkeys.py')
api = meetup.client

#1. Pick a search criteria for groups. 

tacos=api.GetFindGroups({"zip" :'78701','text': "tacos"}) #zipcode for the capitol in Austin
#11 groups in zipcode 78701 related to tacos

#Find the group with the most members: there is an argument 'members' for .GetFindGroups, but I don't know how it works; it doesn't order the list of MeetUp objects like it should 
# I know there is a better way to do this, but I do not know what that way is
# There are few groups in my search, but were there many groups, I believe this would work
most_members=max([i.members for i in tacos]) #find the max number of members
[i for i,j in enumerate(num_of_members) if j==most_members]
#get the index of the group with the most members
tacos[9].urlname 

#Trailer-Friends has 6986 members.

#2. Which member is the most active?
taco_members=api.GetMembers({'group_urlname':'Trailer-Friends'})
#member objects
ppl=taco_members.__dict__['results']
ppl_ids=[i['id'] for i in ppl] 
number_of_groups=[]
import time
#write a while loop that creates a list of tuples where the first item
# is the member id and the second is the number of groups the member is in 
number_of_groups=[]
timebreak=True
while timebreak:
	for i in ppl_ids:
		try:
			number_of_groups.append((i,api.GetGroups({'member_id':str(i)}).meta['total_count'] ))
			timebreak=False
		except: 
			time.sleep(8)
			continue
		if len(number_of_groups)==200: break

#find the max number of groups: search index 1 of tuples
from operator import itemgetter
max(number_of_groups,key=itemgetter(1))

#member id 200756197 is in 232 groups


#3. Of the active members, which group is the most popular?
guy.results
mem_in_groups=[]
for i in guy.results:
	mem_in_groups.append((i['name'],i['members'] ))
max(mem_in_groups,key=itemgetter(1))

#The group with the most number of members that Taco Guy is in is NY Tech Meetup with 59637 members