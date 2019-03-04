#Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file
import os,re
#TODO: find occurrences and prompt user to replace them

#TODO: print out text



#TODO: Ask for file name to read and save result to a new text file
fileName = input('Please enter the name of the template file you wish to use:  ')
lib = open('{0}/{1}.txt'.format(os.getcwd(), fileName))
string = lib.read()