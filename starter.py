#!/usr/bin/python
'''
Starter file to test wff-pl-module.

Author:
	kinzang chhogyal (kindrix@gmail.com)
'''

#import wffModule

import parser
import ttable


#-------------------------------------------------------------------------------------------#
# find alphabet given formula
#-------------------------------------------------------------------------------------------#

def get_alphabet(symList):

	alphabet =[]

	for item in symList:
		if (not(item[1] in alphabet) and item[1].isalpha()):
			alphabet.append(item[1].lower())  #make lowercase and add to alphabet

	return alphabet

#functin show_truth_table

def show_truth_table(alphabet, sentence, possibleWorldsTable, truthValues):
	print '\n-- Truth Table -- \n'
	for item in alphabet:
		print item, ' | ',  
	print sentence,
	print '\n-------------------------------------------------'
	for i in range(len(truthValues)):
		possibleWorld = possibleWorldsTable[i]
		for item in alphabet:
			print possibleWorld[item], ' | ',
		print '    ', truthValues[i]


#-------------------------------------------------------------------------------------------#
#  main program
#-------------------------------------------------------------------------------------------#

exp = raw_input('Enter sentence: ')

#check if exp is wff and return parse tree
parserResult = parser.parse_wff(exp)

if (parserResult[0]):

	#get alphabet
	alphabet = list(get_alphabet(parserResult[3]))
	alphabet.sort()

	#generate possible worlds and get truth table

	ttResult = ttable.get_truth_table(parserResult[3], alphabet)
	truthValues = ttResult[1]
	possibleWorldsTable = ttResult[0]
	
	print '\nAlphabet: ', alphabet

	print '\nInput as list: ', parserResult[4]
	
	print '\nParse Tree: ', parserResult[3]

	print '\nMax depth of parse tree: ', parserResult[2]

	# #display truth table
	show_truth_table(alphabet, ''.join(parserResult[4]), possibleWorldsTable, truthValues)

else:
	print('Oops! Formula is not a wff.')





