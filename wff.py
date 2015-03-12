#!/usr/bin/python

#-------------------------------------------------------------------------------------------#
# Author: Kinzang Chhogyal
# Email: kindrix@gmail.com
#
# Checks if a formula is a well formed formula of propositional logic.
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

def consume_formula(remList):
	#remListCopy = list(remList)
	#print 'current list:', remList

	#cosume an atom
	#formula: atom

	is_atom, remList = consume_atom(remList)
	if is_atom:
		return 1, remList


	#consume negation followed by formula
	#formula: ~ formula

	is_negation, remList = consume_negation(remList)
	if is_negation:
		is_formula, remList = consume_formula(remList)
		if is_formula:
			return 1, remList


	#consume an opening bracket followed by a formula, operator and a closing bracket
	#formula: (formula operator formula)

	is_open_bracket, remList = consume_open_bracket(remList)
	if is_open_bracket:
		is_formula, remList = consume_formula(remList)
		if is_formula:
			is_operator, remList = consume_operator(remList)
			if is_operator:
				is_formula, remList = consume_formula(remList)
				if is_formula:
					is_closing_bracket, remList = consume_closing_bracket(remList)
					if is_closing_bracket:
						return 1, remList
	#all rules fails
	return 0, remList


# consume an atom and return remaining list

def consume_atom(remList):
	if (len(remList) == 0):
		return 0, remList
	if ( remList[0].isalpha() ):
		remList.remove(remList[0])
		return 1, remList
	return 0, remList

# consume negation symbol and return remaining list

def consume_negation(remList):
	if (len(remList) == 0):
		return 0, remList
	if ( remList[0] == '~' ):
		remList.remove(remList[0])
		return 1, remList
	return 0, remList


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
		return 0, remList
	#and, or
	if ( remList[0] in ['&', '|']  ):
		remList.remove(remList[0])
		return 1, remList
	#implication
	elif (remList[0] == '-' and remList[1] == '>'):
		remList.remove(remList[0])
		remList.remove(remList[0])
		return 1, remList
	#biconditional
	elif (remList[0] == '<' and remList[1] == '-' and remList[2] == '>'):
		remList.remove(remList[0])
		remList.remove(remList[0])
		remList.remove(remList[0])
		return 1, remList
	return 0, remList


#-------------------------------------------------------------------------------------------#
#main function to check if formula is valid
#returns 1 if valid , 0 otherwise
#-------------------------------------------------------------------------------------------#

def checkWFF(exp):
	exp = exp.lower()
	remList = stringToCharList(exp)
	symList = list(remList)
	is_formula, remList = consume_formula(remList)
	if (is_formula and len(remList) == 0):
		return is_formula, symList
	return 0, symList

# #program execution starts here

# exp = raw_input('Enter sentence:')
# #exp = 'a & b'
# print '\nChecking expression: %s ' %exp
# if checkWFF(exp):
# 	print('valid')
# else:
# 	print('invalid')




