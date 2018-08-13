import unittest

from Ang_lab03 import *

class labTests(unittest.TestCase):
	
	## fill in a few tests for each
	## make sure to account for correct and incorrect input

    def test_shout(self):
     	self.assertEqual('NO', shout('no'))
        with self.assertRaises(AttributeError):
            shout(42)
    	with self.assertRaises(AttributeError):
            shout([101, 'dalmatians'])
    def test_reverse(self):
    	self.assertEqual('edcba', reverse('abcde'))
    def test_reversewords(self):
    	self.assertEqual('all for one', reversewords('one for all'))
    def test_reversewordletters(self):
    	self.assertEqual('ecar rac', reversewordletters('race car'))
    def test_piglatin(self):
    	self.assertEqual('oystay', piglatin('toys'))

if __name__ == '__main__':
  unittest.main()

### Question: What is the difference between an AttributeError
# and a TypeError? An AttributeError relates to functions that use a '.',
# like in my_list.append?
# https://docs.python.org/2/library/exceptions.html