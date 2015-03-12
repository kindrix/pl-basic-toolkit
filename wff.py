#!/usr/bin/python

'''Checks if string is a well-formed-formula

This module checks if an given expression is a well formed formula (wff) of propositional logic (PL).
Based on Prolog style definite clause grammar (DCG) implemented used difference lists. To learn 
more about DCG and Prolog go to http://www.learnprolognow.org/lpnpage.php?pagetype=html&pageid=lpn-htmlse28.

Propositional Logic Language:
	A PL language consists of all sentences (formula) that can be generated from a set of 
	alphabets (atoms) using the recursive rules below:

	formula -> atom
	formula -> ~ formula
	formula -> (formula   operator  formula)
	operator -> {&, |, ->, <->} 
	atom -> {a, c, d, ...z, A .. Z}

	Examples of valid and invalid formulas:
	a : valid
	~b : valYou can call it as follows:
	check_wff()
	~(c): invalid
	~(c & d) : valid
	(c & d :invalid
	((c & d ) -> (b & ( e -> f)) ) : valid

Usage Example:
	The main funciton is called check_wff(exp) which takes 1 argument which is a string.
	The main function check_wff returns a tuple with two items. The first item is a boolean value 
	that indicates whether the sentece is a wff (1) or not (0). The second item is just the
	input string represented as a list of chars.

	Ex.1 Valid wff
	>>> import wff
	>>> a =  '( ~a -> (b | c))'
	>>> wff.check_wff(a)
	(1, ['(', '~', 'a', '-', '>', '(', 'b', '|', 'c', ')', ')'])

    Ex.2 Invalid wff
    >>> a = '(a->b'
	>>> wff.check_wff(a)
	(0, ['(', 'a', '-', '>', 'b'])


Author:
	kinzang chhogyal (kindrix@gmail.com)

'''

#-------------------------------------------------------------------------------------------#
#Checking if a sentence is a wff of propositinonal logic.
#author: kinzang chhogyal (kindrix@gmail.com)
#license: mit
#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------#


def str_to_char_list(exp):
	'''Takes a string and return a list of chars after removing spaces. '''

	charList = []
	for char in exp:
		if (not(char == ' ')):
			charList.append(char)
	return charList


#-------------------------------------------------------------------------------------------#

def consume_formula(remList):
	'''Recursive defintion of a valid formula (wff).

	Args:
      remlist (list): List of symbols that make up sentence (chars)

    Returns:
      bool: True if wff, False otherwise.
      list: Remainder list after consumption according to grammar rules.

	'''

	#Cosume an atom and return remainder.
	#Rule: formula -> atom

	is_atom, remList = consume_atom(remList)
	if is_atom:
		return 1, remList


	#Consume negation followed by formula and return remainder.
	#Rule: formula -> ~ formula

	is_negation, remList = consume_negation(remList)
	if is_negation:
		is_formula, remList = consume_formula(remList)
		if is_formula:
			return 1, remList


	#Consume an opening bracket followed by a formula, operator and a closing bracket.
	#Rule: formula -> (formula operator formula)

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
	#all rules fail
	return 0, remList

#-------------------------------------------------------------------------------------------#

def consume_atom(remList):
	'''Consume an atom and return remaining list.'''

	if (len(remList) == 0):
		return 0, remList
	if ( remList[0].isalpha() ):
		remList.remove(remList[0])
		return 1, remList
	return 0, remList

#-------------------------------------------------------------------------------------------#
def consume_negation(remList):
	'''Consume negation and return remaining list.'''

	if (len(remList) == 0):
		return 0, remList
	if ( remList[0] == '~' ):
		remList.remove(remList[0])
		return 1, remList
	return 0, remList

#-------------------------------------------------------------------------------------------#

def consume_open_bracket(remList):
	'''Consume an open bracket '(' and return remaining list.'''

	if (len(remList) == 0):
		return 0, remList
	if ( remList[0] == '(' ):
		remList.remove(remList[0])
		return 1, remList
	return 0, remList

#-------------------------------------------------------------------------------------------#

def consume_closing_bracket(remList):
	'''Consume losing bracket ')' and  return remaining list.'''

	if (len(remList) == 0):
		return 0, remList
	if (remList[0] == ')' ):
		remList.remove(remList[0])
		return 1, remList
	return 0, remList

#-------------------------------------------------------------------------------------------#

def consume_operator(remList):
	'''Consume an operator and return remaining list.'''

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
#main function
#-------------------------------------------------------------------------------------------#

def check_wff(exp):
	'''Check if string is a well-formed-formula (wff).

	This is the main function for this module.

	Args:
      exp (string): possible sentence of language

    Returns:
      bool: True if wff, False otherwise.
      list: Remainder list after consumption according to grammar rules

	'''

	exp = exp.lower()
	remList = str_to_char_list(exp)
	symList = list(remList)
	is_formula, remList = consume_formula(remList)
	if (is_formula and len(remList) == 0):
		return is_formula, symList
	return 0, symList





