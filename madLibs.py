#Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file

import os,re


# and prompt user to replace them

#TODO: print out text



# Ask for file name to read and save result to a new text file
fileName = input('Please enter the name of the template file you wish to use:  ')
lib = open('{0}/{1}.txt'.format(os.getcwd(), fileName))
string = lib.read()

#find occurrences
replace = 0
madlib = re.compile(r'(NOUN|VERB|ADVERB|ADJECTIVE)')
matche = madlib.findall(string)