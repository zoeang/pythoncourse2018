## Trick and explanation of base conversion
## http://www.purplemath.com/modules/base_why.htm

"""convert positive integer to base 2"""

def binarify(num):
        digits=[]
    while num>0:
        digits.append(num%2)
        num=num/2
    print ''.join([str(i) for i in digits[::-1]]) #can remove the brackets and this will still be a list

"""convert positive integer to a string in any base"""
#need a method/ error warning for bases: negative, 10, and 1
def int_to_base(num, base):
    digits=[]
    while num>0:
        digits.append(num%base)
        num=num/base
    print ''.join([str(i) for i in digits[::-1]])

"""take a string-formatted number and its base and return the base-10 integer"""
def base_to_int(string, base):
    #break string into individual characters
    #convert characters to integers
    #multiply that integer by the base raised to the index of the integer
    #add the numbers together 
    digits=[ int(i) for i in string] #digits in now a list where each
                                #element is an integer
    #exps=range(len(digits)-1,-1,-1) #this is the largest exponent
                            #the number with this exp will be the 0 index
    places=[] #create an empty list of the places
              #the elements will eventually be summed
    for i in digits:
        places.append(i*(base**exps))#this is wrong
                                     #i is the number in the list digits
                                     #i need to iterate over the values of exp as well


"""add two numbers of different bases and return the sum"""
def flexibase_add(str1, str2, base1, base2):


"""multiply two numbers of different bases and return the product"""
def flexibase_multiply(str1, str2, base1, base2):


"""given an integer, return the Roman numeral version"""
def romanify(num):

  
# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.