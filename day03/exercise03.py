## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer
## When done, run the test file in the terminal and see your results.
def count_vowels(word):
	if (type(word)==str)==False:
		raise TypeError, "Enter a string."
	else:
		vowels= ['a','e','i','o','u'] #list of vowels
		word_letters=[i for i in word] #store each letter of the word as an element of a list
		number_of_vowels=0 
		for i in word_letters: #for each letter in the word
			if i in vowels: #check if the letter is in the list of vowels
				#print i + ' is a vowel.'
				number_of_vowels+=1
		return number_of_vowels



# to run, navigate to file