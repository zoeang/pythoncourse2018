import re

# open text file of 2008 NH primary Obama speech
with open("obama-nh.txt", "r") as f:
	obama = f.readlines()


## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]
pattern = re.compile(r"\s?[tT]he\s")
for l in obama:
	if pattern.search(l):
		pass
	else:
		print l

output=[l for l in obama if not pattern.search(l)]


# TODO: print lines that contain a word of any length starting with s and ending with e

pattern1=re.compile(r'\b[sS][a-z]*e[\s\.]')
output1=[l for l in obama if pattern1.search(l)]

# This would not capture lines that started with a word of interest
#pattern2=re.compile(r'\s[sS][a-z]*e[\s\.]')

## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY
date = raw_input("Please enter a date in the format MM.DD.YY: ")
pattern3=re.compile(r'(\d{2})\.(\d{2})\.(\d{2})')
unit=pattern3.search(date.encode('utf-8'))
print 'Month: ' + unit.group(1) + '\n' + 'Day: ' +unit.group(2) + '\n'+'Year: ' +unit.group(3)


