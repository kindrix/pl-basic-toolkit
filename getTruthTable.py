#!/usr/bin/python

#import wffModule

import wffParserPropLogic
import generatePossibleWorlds


#-------------------------------------------------------------------------------------------#
# find element at given depth
#-------------------------------------------------------------------------------------------#

def findElementAtDepth(parseTree, depth):
	for i in range(0, len(parseTree)):
		if parseTree[i][0] == depth:
			return i
	return 0

#-------------------------------------------------------------------------------------------#
# evaluate truth value returned by parse tree after
# replacing atom by True or False from a particular
# row of truth table
#-------------------------------------------------------------------------------------------#

def evaluateParseTree(parseTree, depth, possibleWorld):

	#find index of element at current depth
	#parseTress is represented as a list of tuples

	elementIndex = findElementAtDepth(parseTree, depth)

	#if element found is negation
	#there is no left branch
	# return negatation of value of right branch

	if (parseTree[elementIndex][1] == '~'):

		rightBranch = parseTree[elementIndex + 1: len(parseTree)]
		rightBranchValue = evaluateParseTree(rightBranch, depth + 1, possibleWorld)
		return not(evaluateParseTree(rightBranch, depth + 1, possibleWorld))

	#if current element is atom
	#return its truth value in current row of truth table

	elif (parseTree[elementIndex][1].islower()):
		return possibleWorld[parseTree[elementIndex][1]]

	#if current element is a boolean connective, 
	#find left and right branch
	#return truth value of right branch

	elif (len(parseTree) > 1):

		leftBranch = parseTree[0:elementIndex]
		rightBranch = parseTree[elementIndex + 1: len(parseTree)]
		leftBranchValue = evaluateParseTree(leftBranch, depth + 1, possibleWorld)
		rightBranchValue = evaluateParseTree(rightBranch, depth + 1,possibleWorld)
		
		if (parseTree[elementIndex][1] == '&'):
			return leftBranchValue and rightBranchValue
		
		elif (parseTree[elementIndex][1] == '|'):
			return leftBranchValue or rightBranchValue
		
		elif (parseTree[elementIndex][1] == '->'):
			return ( not(leftBranchValue) or rightBranchValue)
		
		else:
			return ( (not(leftBranchValue) or rightBranchValue) and (not(rightBranchValue) or leftBranchValue))


#
def getTruthTable(result, alphabet):

	# #check if exp is wff and return parse tree
	# result = wffParserPropLogic.parseWFF(exp)
	# print 'result:', result
	#if (result[0]):

	#get alphabet
	#alphabet = list(getAlphabet(result[3]))
	#alphabet.sort()

	#generate possible worlds
	possibleWorldsTable = generatePossibleWorlds.generatePossibleWorlds(alphabet)

	print '\nFormula is valid'
	print 'symlist: ', result[1]
	print 'Max depth: ', result[2]
	print 'Parse Tree: ', result[3]
	print 'Sorted Parse Tree', sorted(result[3])

	#evaluate truth value of formula using parse tree
	startDepth = 0
	truthValues =[]
	print '\n', possibleWorldsTable
	for possibleWorld in possibleWorldsTable:
		#convert True to int
		isModel = int(evaluateParseTree(result[3], startDepth, possibleWorld))
		truthValues.append(isModel)
	# displayTruthTable(alphabet, ''.join(result[4]), possibleWorldsTable, truthValues)
	# else:
	# 	print('Oops! Formula is not a wff.')
	return possibleWorldsTable, truthValues


#functin displayTruthTable

# def displayTruthTable(alphabet, sentence, possibleWorldsTable, truthValues):
# 	print '\nTruth Table \n'
# 	for item in alphabet:
# 		print item, ' | ',  
# 	print sentence,
# 	print '\n-------------------------------------------------'
# 	for i in range(len(truthValues)):
# 		possibleWorld = possibleWorldsTable[i]
# 		for item in alphabet:
# 			print possibleWorld[item], ' | ',
# 		print '    ', truthValues[i]


