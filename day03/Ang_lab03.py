import string
## 1. write tests in lab03_tests.py
## 2. then code for the following functions

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int


## make all characters capitalized
def shout(txt):
	print txt.upper()


## reverse all characters in string
def reverse(txt):
	if (type(txt)==str)==False: #wuut?
		raise TypeError, "Argument must be a string."
	else:
		forward=[i for i in txt]
		forward.reverse()
		return ''.join(forward)


## reverse word order in string
def reversewords(txt):
	word_list=txt.split(' ')
	word_list.reverse()
	return " ". join(word_list)
## reverses letters in each word
def reversewordletters(txt):
	return reverse(reversewords(txt))
	
## change text to piglatin.. google it! 
def piglatin(txt):
	word_list=txt.split(' ')
	piglatin_words=[]
	for i in word_list:
		piglatin_string=i[1:]+i[0]+'ay'
		piglatin_words.append(piglatin_string)
	for i in piglatin_words:
		return ' '.join(piglatin_words)


# Try/catch is more common when using
# someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
 
string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]

def test_string_list (string_list):
	for i in string_list:
		try:
			reverse(i)
		except TypeError as err:
			print err
		
			
			
			
			
			
			

