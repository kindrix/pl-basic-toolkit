#!/usr/bin/python
'''Given a string, checks if it is wff and builds a parse tree.

This module checks if an given expression is a well formed formula (wff) of propositional logic (PL)
and it also returns a parse tree. Based on Prolog style definite clause grammar (DCG) implemented 
used difference lists. To learn more about DCG and Prolog go to 
http://www.learnprolognow.org/lpnpage.php?pagetype=html&pageid=lpn-htmlse28.

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
	The main funciton is called parse_wff(exp) which takes 1 argument which is a string.
	The main function check_wff returns a tuple with 5 items. 

	Ex.1 Valid wff
	>>> a ='(a->(b&c))'
	>>> parser.parse_wff(a)
	(
		1, 
	 	[],
	 	2,
	 	[(1, 'a'), (0, '->'), (2, 'b'), (1, '&'), (2, 'c')],
	 	['(', 'a', '-', '>', '(', 'b', '&', 'c', ')', ')']
	)

    Ex.2 Invalid wff
    >>> a ='(a->b'
	>>> parser.parse_wff(a)
	(
		0, 
		[], 
		0, 
		[(1, 'a'), (0, '->'), (1, 'b')],
		['(', 'a', '-', '>', 'b']
	)

Author:
	kinzang chhogyal (kindrix@gmail.com)

'''


#-------------------------------------------------------------------------------------------#

def str_to_char_list(exp):
	'''Takes a string and return a list of chars after removing spaces. '''

	charList = []
	for char in exp:
		if (not(char == ' ')):
			charList.append(char)
	return charList


#-------------------------------------------------------------------------------------------#
# recursive definition of a wff
#-------------------------------------------------------------------------------------------#

def consume_formula(remList, depth, parseTree):
	'''Recursive defintion of a valid formula (wff).

	Args:
      remlist (list): List of symbols that make up sentence  (chars).
      depth (int): Current depth of parse tree. Main connector of sentence has 
      			   depth 0. Eg. In (a -> b), -> has depth 0. a and b have depth 1.
      parseTree (list of tuples): First item of tuple is depth, second item is symbol.

    Returns:
      bool: True if wff, False otherwise.
      list: Remainder list after consumption according to grammar rules.
      int:  Maximum depth of parse tree.

	'''
	
	#Cosume an atom and return remainder.
	#Rule: formula -> atom.

	is_atom, remList, atom = consume_atom(remList)
	if is_atom:
		parseTree.append((depth, atom))
		return 1, remList, depth


	#Consume negation followed by formula and return remainder.
	#Rule: formula -> ~ formula.

	is_negation, remList, negation = consume_negation(remList)
	if is_negation:
		parseTree.append((depth, negation))
		is_formula, remList, depth = consume_formula(remList, depth + 1, parseTree)
		if is_formula:			
			return 1, remList, depth


	#Consume an opening bracket followed by a formula, operator and a closing bracket.
	#Rule: formula -> (formula operator formula).

	is_open_bracket, remList = consume_open_bracket(remList)
	if is_open_bracket:
		currentDepth = depth #Copy made for right branch of prase tree.

		#Check left branch is wff and increase depth by 1.
		is_formula, remList, leftDepth = consume_formula(remList, depth + 1, parseTree)

		if is_formula:
			is_operator, remList, operator = consume_operator(remList)
			if is_operator:
				parseTree.append((currentDepth, operator))

				#Check right branch is wff and use the copy of depth (currentDept).
				is_formula, remList, rightDepth = consume_formula(remList, currentDepth + 1, parseTree)
				
				if is_formula:
					is_closing_bracket, remList = consume_closing_bracket(remList)
					if is_closing_bracket:

						#Compare left and right branch to find max depth.
						if (leftDepth > rightDepth):
							depth =  leftDepth
						else:
							depth = rightDepth
						return 1, remList, depth
	#If all rules fails
	return 0, remList, depth

#-------------------------------------------------------------------------------------------#

# consume an atom and return remaining list

def consume_atom(remList):
	'''Consume atom.

	Args:
      remlist (list): List of symbols that make up sentence  (chars).

    Returns:
      bool: True if atom, False otherwise.
      list: Remainder list after consuming atom.
      char: The atom consumed to build parse tree.

	'''

	if (len(remList) == 0):
		return 0, remList, None
	if ( remList[0].isalpha() ):
		atom = remList[0]
		remList.remove(remList[0])
		return 1, remList, atom
	return 0, remList, None

#-------------------------------------------------------------------------------------------#

def consume_negation(remList):
	'''Consume atom.

	Args:
      remlist (list): List of symbols that make up sentence  (chars).

    Returns:
      bool: True if '~' consumed, False otherwise.
      list: Remainder list after consuming atom.
      char: '~' to build parse tree.

	'''

	if (len(remList) == 0):
		return 0, remList, None
	if ( remList[0] == '~' ):
		negation = remList[0]
		remList.remove(remList[0])
		return 1, remList, negation
	return 0, remList, None

#-------------------------------------------------------------------------------------------#

def consume_open_bracket(remList):
	''' Similar to previous operators. '''

	if (len(remList) == 0):
		return 0, remList
	if ( remList[0] == '(' ):
		remList.remove(remList[0])
		return 1, remList
	return 0, remList

#-------------------------------------------------------------------------------------------#

def consume_closing_bracket(remList):
	''' Similar to previous operators. '''

	if (len(remList) == 0):
		return 0, remList
	if (remList[0] == ')' ):
		remList.remove(remList[0])
		return 1, remList
	return 0, remList

#-------------------------------------------------------------------------------------------#

def consume_operator(remList):
	''' Similar to previous operators except operator is returned. '''

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
#main function
#-------------------------------------------------------------------------------------------#

def parse_wff(exp):
	'''Parse a string and check if wff and build parse tree.

	Args:
      exp: String to be checked if wff.

    Returns:
      bool: True if wff, False otherwise.
      list: Remainder list after consumption according to grammar rules.
      int:  Maximum depth of parse tree.
      tuple-list: First item of tuple is depth, second is terminal symbol.
      list: Input string 'exp' represented as list so it can be used by other modules.

	'''
	exp = exp.lower()
	remList = str_to_char_list(exp)
	symList = list(remList)
	startDepth = 0
	parseTree = []
	is_formula, remList, depth = consume_formula(remList, startDepth, parseTree)
	if (is_formula and len(remList) == 0):
		return is_formula, remList, depth, parseTree, symList
	return 0, remList, depth, parseTree, symList





