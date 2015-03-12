#!/usr/bin/python

#import wffModule

import wffParserPropLogic
import getTruthTable


#-------------------------------------------------------------------------------------------#
# find alphabet given formula
#-------------------------------------------------------------------------------------------#

def getAlphabet(symList):

	alphabet =[]

	for item in symList:
		if (not(item[1] in alphabet) and item[1].isalpha()):
			alphabet.append(item[1].lower())  #make lowercase and add to alphabet

	return alphabet

#functin displayTruthTable

def displayTruthTable(alphabet, sentence, possibleWorldsTable, truthValues):
	print '\nTruth Table \n'
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
parserResult = wffParserPropLogic.parseWFF(exp)



if (parserResult[0]):

	#get alphabet
	alphabet = list(getAlphabet(parserResult[3]))
	alphabet.sort()

	ttResult = getTruthTable.getTruthTable(parserResult, alphabet)
	truthValues = ttResult[1]
	possibleWorldsTable = ttResult[0]
	

	# #generate possible worlds
	# possibleWorldsTable = generatePossibleWorlds.generatePossibleWorlds(alphabet)

	# print '\nFormula is valid'
	# print 'symlist: ', parserResult[1]
	# print 'Max depth: ', parserResult[2]
	# print 'Parse Tree: ', parserResult[3]
	# print 'Sorted Parse Tree', sorted(parserResult[3])

	# #evaluate truth value of formula using parse tree
	# startDepth = 0
	# truthValues =[]
	# print '\n', possibleWorldsTable

	# #for each possible world, evaluate formula
	# for possibleWorld in possibleWorldsTable:
	# 	#convert True to int
	# 	isModel = int(evaluateParseTree(parserResult[3], startDepth, possibleWorld))
	# 	truthValues.append(isModel)

	# #display truth table
	displayTruthTable(alphabet, ''.join(parserResult[4]), possibleWorldsTable, truthValues)

else:
	print('Oops! Formula is not a wff.')





