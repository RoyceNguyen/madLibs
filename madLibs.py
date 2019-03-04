#Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file

import os,re

# Ask for file name to read and save result to a new text file
fileName = input('Please enter the name of the template file you wish to use:  ')
#/ for OS , \ for windows
lib = open('{0}\{1}.txt'.format(os.getcwd(), fileName))
string = lib.read()

#find occurrences
replace = 0
madlib = re.compile(r'(NOUN|VERB|ADVERB|ADJECTIVE)')
match = madlib.findall(string)

#for each word found prompt user for a word then replace it in the string
for word in match:
    subString = input('Enter a' + word + ': ')
    string = string.replace(word, subString, 1)

print(string)