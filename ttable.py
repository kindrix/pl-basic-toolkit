#!/usr/bin/python

'''Generates truth table given parseTree and alphabet.

This module must be used in conjuction with the 'parser' and 'worlds modules'.

The main function is get_truth_table/2.

Usage example:
	Consider the following formuala '(a& b)'.

	>>> parseTree= [(1, 'a'), (0, '&'), (1, 'b')]
	>>> alphabet = ['a', 'b']
	>>> ttable.get_truth_table(parseTree, alphabet)
	(
		[{'a': 0, 'b': 0},
		 {'a': 0, 'b': 1}, 
		 {'a': 1, 'b': 0}, 
		 {'a': 1, 'b': 1}
		], 
		[0, 0, 0, 1])

	The first list shows the possible worlds. The second list shows the truth value of '(a & b)'
	at each possible world. For instance in the first world where a and b are false, the first item
	in the second list is also false. 

Author:
	kinzang chhogyal (kindrix@gmail.com).

'''

import parser
import worlds


#-------------------------------------------------------------------------------------------#

def get_item_at_depth(parseTree, depth):
	'''Finds symbol at given depth of parse tree.
	'''

	for i in range(0, len(parseTree)):
		if parseTree[i][0] == depth:
			return i
	return 0

#-------------------------------------------------------------------------------------------#

def eval_parse_tree(parseTree, depth, possibleWorld):
	'''Uses parse tree of formula to check whether the possible world is a model of formula.

	This is done recursively by evaulating the left and right branch until we get to an atom
	or a negation symbol.

	Args:
		parseTree (tuple-list): Parse tree of sentence. Tuple consists of depth and symbol
		depth (int): Current depth of parse tree.
		possibleWorld(dict): Dictionary represents possible world.

	Returns:
		bool: True if possibleWorld is a model of formula (parse tree).


	'''

	#find index of element at current depth

	elementIndex = get_item_at_depth(parseTree, depth)

	#If element found is negation, there is no left branch.
	#Return negatation of value of right branch

	if (parseTree[elementIndex][1] == '~'):

		rightBranch = parseTree[elementIndex + 1: len(parseTree)]
		rightBranchValue = eval_parse_tree(rightBranch, depth + 1, possibleWorld)
		return not(eval_parse_tree(rightBranch, depth + 1, possibleWorld))

	#If current element is atom, return its truth value in possible world.

	elif (parseTree[elementIndex][1].islower()):
		return possibleWorld[parseTree[elementIndex][1]]

	#If current element is a boolean connective, find truth value of left and right branch.
	#Return combine truth value of the two branches using connective.

	elif (len(parseTree) > 1):

		leftBranch = parseTree[0:elementIndex]
		rightBranch = parseTree[elementIndex + 1: len(parseTree)]
		leftBranchValue = eval_parse_tree(leftBranch, depth + 1, possibleWorld)
		rightBranchValue = eval_parse_tree(rightBranch, depth + 1,possibleWorld)
		
		if (parseTree[elementIndex][1] == '&'):
			return leftBranchValue and rightBranchValue
		
		elif (parseTree[elementIndex][1] == '|'):
			return leftBranchValue or rightBranchValue
		
		elif (parseTree[elementIndex][1] == '->'):
			return ( not(leftBranchValue) or rightBranchValue)
		
		else:
			return ( (not(leftBranchValue) or rightBranchValue) and (not(rightBranchValue) or leftBranchValue))


#-------------------------------------------------------------------------------------------#


def get_truth_table(parseTree, alphabet):
	'''Returns truth table given parseTree and alphabet.

	Args:
		parseTree (tuple-list): Parse tree of sentence. Tuple consists of depth and symbol
		alphabet: List of atoms. Used to generate possible worlds.
	Returns:
		dict-list: Dictionary represents possible world. List contains all worlds.
		truthValues: Truth value of sentence evaluated at each possibleWorld.
	'''

	#get possible worlds
	possibleWorldsTable = worlds.get_poss_worlds(alphabet)


	#evaluate truth value of formula using parse tree
	startDepth = 0   #depth of main connective
	truthValues =[]  #truth value of formula evaluated at a particular world 
	
	for possibleWorld in possibleWorldsTable:
		isModel = int(eval_parse_tree(parseTree, startDepth, possibleWorld)) #convert True to int
		truthValues.append(isModel)

	return possibleWorldsTable, truthValues



