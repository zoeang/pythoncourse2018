#====================================================================
# Homework 4
#====================================================================
#Sorting Algorithms
# Algorithm 1: Bubble sorting; best caseO(n), worst case O(n^2)

def bubble(n): # n is a list
	for i in range(0, len(n)-1):
		if n[i]>n[i+1]:
			placeholder=n[i]
			n[i]=n[i+1]
			n[i+1]=placeholder
		else: pass
	return n

# Algorithm 2: Merge sorting ; best and worst case O(n log n) ---------------------------------
# Need help debugging: dropping first element of arugment list
#====================================================================
def merge(left, right):
	output=[]
	while len(left)>0 and len(right)>0:
		if left[0]<=right[0]:
			output.append(left[0])
			left.remove(left[0])
		else: 
			output.append(right[0])
			right.remove(right[0])
	#there will be one element remaining in either the left or right list
	#the loop relating to the list with the final element will be entered
	if len(left)>0:
		output.append(left[0])
		#print 'left list'
	if len(right)>0:
		output.append(right[0])
		#print 'rightlist'
	return output ###says that there should be an indent here, but there shouldn't be...

def merge_sort(l):
	if len(l)<=1:
		return l
	left=[]
	right=[]
	for i in range(len(l)):
		if i%2!=0:
			left.append(l[i])
		else: right.append(l[i])
	leftlist=merge_sort(left)
	#print str(leftlist) +'\t left'
	rightlist=merge_sort(right)
	#print str(rightlist) + '\t right'
	return merge(leftlist, rightlist)
# Funtion to time algorithms---------------------------------------------

# Returns tuple of time and length of arg and time (tuple will be (x,y) point for ploting)
import timeit
def timealg(func,arg): #func is the name of the function, arg is the input to the argument
	start= timeit.default_timer()
	func(arg)
	end=timeit.default_timer()
	return len(arg), end-start

#generate data to plot
#the first list returned is the bubble alg, the second, merge sorting alg
from random import uniform 
lis=[1]
def dat(lis):
	bub=[]
	merge_alg=[]
	while len(lis)<100:
		bub.append(timealg(bubble,lis))
		merge_alg.append(timealg(merge_sort, lis))
		lis.append(int(uniform(1,100)))
	return [bub, merge_alg]
