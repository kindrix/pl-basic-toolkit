#!/usr/bin/python

#-------------------------------------------------------------------------------------------#
# Author: Kinzang Chhogyal
# Email: kindrix@gmail.com
#
# Produces parse tree of a well formed formula of propositional logic.
# Same as checkWFF.py except it also produces parse tree as a list of tuples.
# Based on DCG in Prolog using difference lists.
# More information about DCG and Prolog at 
# http://www.learnprolognow.org/lpnpage.php?pagetype=html&pageid=lpn-htmlse28.


#The following are the wff rules that I've used:

# formula : atom
# formula : ~ formula
# formula : (formula   operator  formula)
# operator : {&, |, ->, <->} 
# atom: a, c, d, ...z

#Examples of valid and invalid formulas:
# a : valid
# ~b : valid
# ~(c): invalid
# ~(c & d) : valid
# (c & d :invalid
# ((c & d ) -> (b & ( e -> f)) ) : valid

# The main function is called parseWFF(exp) and takes one argument 'exp'
# which is a string representaion of a formula and it returns a tuple of four items:
# 1) is_formula - true if valid wff
# 2) remList - remaining list after consumption of atoms and connectives
# 3) depth    - the max depth of the parse tree
# 4) parseTree  - the parse tree

#-------------------------------------------------------------------------------------------#


#-------------------------------------------------------------------------------------------#
#return list of chars and also remove spaces
#-------------------------------------------------------------------------------------------#
def stringToCharList(exp):
	charList = []
	for char in exp:
		if (not(char == ' ')):
			charList.append(char)
	return charList


#-------------------------------------------------------------------------------------------#
# recursive definition of a wff
#-------------------------------------------------------------------------------------------#

def consume_formula(remList, depth, parseTree):
	#remListCopy = list(remList)
	#print 'current list:', remList

	#cosume an atom
	#formula: atom

	is_atom, remList, atom = consume_atom(remList)
	if is_atom:
		parseTree.append((depth, atom))
		return 1, remList, depth


	#consume negation followed by formula
	#formula: ~ formula

	is_negation, remList, negation = consume_negation(remList)
	if is_negation:
		parseTree.append((depth, negation))
		is_formula, remList, depth = consume_formula(remList, depth + 1, parseTree)
		if is_formula:			
			return 1, remList, depth


	#consume an opening bracket followed by a formula, operator and a closing bracket
	#formula: (formula operator formula)

	is_open_bracket, remList = consume_open_bracket(remList)
	if is_open_bracket:
		currentDepth = depth
		is_formula, remList, leftDepth = consume_formula(remList, depth + 1, parseTree)
		if is_formula:
			is_operator, remList, operator = consume_operator(remList)
			if is_operator:
				parseTree.append((currentDepth, operator))
				is_formula, remList, rightDepth = consume_formula(remList, currentDepth + 1, parseTree)
				if is_formula:
					is_closing_bracket, remList = consume_closing_bracket(remList)
					if is_closing_bracket:
						if (leftDepth > rightDepth):
							depth =  leftDepth
						else:
							depth = rightDepth
						return 1, remList, depth
	#all rules fails
	return 0, remList, depth


# consume an atom and return remaining list

def consume_atom(remList):
	if (len(remList) == 0):
		return 0, remList, None
	if ( remList[0].isalpha() ):
		atom = remList[0]
		remList.remove(remList[0])
		return 1, remList, atom
	return 0, remList, None

# consume negation symbol and return remaining list

def consume_negation(remList):
	if (len(remList) == 0):
		return 0, remList, None
	if ( remList[0] == '~' ):
		negation = remList[0]
		remList.remove(remList[0])
		return 1, remList, negation
	return 0, remList, None


# consume an open bracket '(' and return remaining list

def consume_open_bracket(remList):
	if (len(remList) == 0):
		return 0, remList
	if ( remList[0] == '(' ):
		remList.remove(remList[0])
		return 1, remList
	return 0, remList

# consume closing bracket ')' and  return remaining list

def consume_closing_bracket(remList):
	if (len(remList) == 0):
		return 0, remList
	if (remList[0] == ')' ):
		remList.remove(remList[0])
		return 1, remList
	return 0, remList

# consume an operator and return remaining list

def consume_operator(remList):
	if (len(remList) == 0):
		return 0, remList, None
	#and, or
	if ( remList[0] in ['&', '|']  ):
		operator = remList[0]
		remList.remove(remList[0])
		return 1, remList, operator
	#implication
	elif (remList[0] == '-' and remList[1] == '>'):
		operator = remList[0] + remList[1]
		remList.remove(remList[0])
		remList.remove(remList[0])
		return 1, remList, operator
	#biconditional
	elif (remList[0] == '<' and remList[1] == '-' and remList[2] == '>'):
		operator = remList[0] + remList[1] + remList[2]
		remList.remove(remList[0])
		remList.remove(remList[0])
		remList.remove(remList[0])
		return 1, remList, operator
	return 0, remList, None

#-------------------------------------------------------------------------------------------#
#main function to check if formula is valid
#returns tuple of 4 items (is_formula, remList, depth, parseTree)
#is_formula = 1 if valid wff , 0 otherwise
#remList = remaining list after consumption
#depth = max. depth of parsetree
#parseTree =  the parseTree as list of tuples
#-------------------------------------------------------------------------------------------#

def parseWFF(exp):
	exp = exp.lower()
	remList = stringToCharList(exp)
	symList = list(remList)
	startDepth = 0
	parseTree = []
	is_formula, remList, depth = consume_formula(remList, startDepth, parseTree)
	if (is_formula and len(remList) == 0):
		return is_formula, remList, depth, parseTree, symList
	return 0, remList, depth, parseTree, symList

#program execution starts here

# exp = raw_input('Enter sentence:')
# #exp = 'a & b'
# print '\nChecking expression: %s ' %exp
# if (parseWFF(exp)[0]):
# 	print('valid')
# else:
# 	print('invalid')




