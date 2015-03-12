#!/usr/bin/python

'''Given alphabet of language as a list generate table of possible worlds
   
   For instance give an alphabet A = {a,b} consisting of two atoms, there are
   four possible worlds dependin on whether a and b are true or false.

   The main function is get_poss_worlds(alphabet).

Usage Example:

 	>>> worlds.get_poss_worlds(['a','b'])
	[{'a': 0, 'b': 0}, {'a': 0, 'b': 1}, {'a': 1, 'b': 0}, {'a': 1, 'b': 1}]

	In the output above, 0 denotes false and 1 denotes true.

Author:
	kinzang chhogyal (kindrix@gmail.com)

'''

#-------------------------------------------------------------------------------------------#

def add_one_bit(possibleWorld, reverseAlphabet):
	'''Find next possible world using bit addition.

	This is done by adding 1 to the previous world.

	Args:
		possibleWorld (dictionary): The previously generated possible world.
		reverseAlphabet (list of chars): The alphabet of the language reversed 
											for technical reasons.

	Returns:
		dictionary: Next possible world.

	'''

	borrow = 1 #bit to be added

	for key in reverseAlphabet:
		if (not borrow):
			return possibleWorld
		else:
			if possibleWorld[key] == 1:
				borrow = 1
				possibleWorld[key] = 0
			else:
				borrow = 0
				possibleWorld[key] = 1
	return possibleWorld


#-------------------------------------------------------------------------------------------#

# add next possible world given by function add_one_bit to list of possible worlds

def add_next_row(possibleWorldsTable, reverseAlphabet):
	'''Calls function add_one_bit and adds the returned possible world 
	   to list of possible worlds.

	   Args:
	   	possibleWorldsTable (dictionary-list): To hold possible worlds.
	   	reverseAlphabet: See above.
	'''

	#find possible world added last
	lastItem = len(possibleWorldsTable) - 1	

	nextPossibleWorld = dict(possibleWorldsTable[lastItem])

	#find next world by adding 1 to last world
	nextPossibleWorld = add_one_bit(nextPossibleWorld, reverseAlphabet)

	possibleWorldsTable.append(nextPossibleWorld)

#-------------------------------------------------------------------------------------------#

def set_initial_row(alphabet):
	'''Set first possible world where all atoms are false.'''

	a ={}
	for item in alphabet:
		a[item] = 0
	return a

#-------------------------------------------------------------------------------------------#

def get_poss_worlds(alphabet):
	'''Main function of module that returns possible world given alphabet.

	Args:
		alphabet: List of atoms.

	Returns:
		dictionary-list: Each dictionary represents a possible world. The list contains
						 all possible worlds.
	'''

	#table of possible worlds
	possibleWorldsTable =[]

	#sort alphabet lexicographically 
	alphabet.sort()

	#reverse alphabet used for generating truth table
	reverseAlphabet = list(alphabet)
	reverseAlphabet.reverse()

	#number of possible worlds
	numPossibleWorld = 2 ** len(alphabet)

	#first possible world - every atom is false
	initialRow =  set_initial_row(alphabet)

	#add first possible world and find rest of possible worlds
	possibleWorldsTable.append(initialRow)
	for i in range (numPossibleWorld - 1):
		add_next_row(possibleWorldsTable, reverseAlphabet)

	#returns a list of possible worlds
	#possible worlds represented as dictionary
	return possibleWorldsTable








