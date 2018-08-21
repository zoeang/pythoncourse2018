#====================================================================
# Homework 4
#====================================================================
#Sorting Algorithms
# Algorithm 1: Bubble sorting; best case O(n log n)

def bubble(n): # n is a list
	for i in range(0, len(n)-1):
		if n[i]>n[i+1]:
			placeholder=n[i]
			n[i]=n[i+1]
			n[i+1]=placeholder
		else: pass
	return n


# Algorithm 2: Merge sorting ; best case O(n)---------------------------------
	# break into dyads

# Funtion to time algorithms---------------------------------------------

# Returns tuple of time and length of arg and time (tuple will be (x,y) point for ploting)
import timeit
def timealg(func,arg): #func is the name of the function, arg is the input to the argument
	start= timeit.default_timer()
	func(arg)
	end=timeit.default_timer()
	return len(arg), end-start
