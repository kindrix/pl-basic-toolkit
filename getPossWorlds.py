#-------------------------------------------------------------------------------------------#
# given alphabet of language as a list generate table of possible worlds
# generatePossibleWorlds(alphabet):
#-------------------------------------------------------------------------------------------#

# Eg :possibleWorlds = [{'a':0, 'b':0},{'a':0, 'b':1}, {'a':1, 'b':0}, {'a':1, 'b':1}] 



# find next possible world given previous possible world addint 1 using boolean arithmetic 

def addOneBit(possibleWorld, reverseAlphabet):
	borrow = 1
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




# add next possible world given by function addOneBit to list of possible worlds

def addNextRow(possibleWorldsTable, reverseAlphabet):
	lastItem = len(possibleWorldsTable) - 1
	nextPossibleWorld = dict(possibleWorldsTable[lastItem])
	nextPossibleWorld = addOneBit(nextPossibleWorld, reverseAlphabet)
	possibleWorldsTable.append(nextPossibleWorld)

#function find first possible world - all atoms false

def generateIntialRow(alphabet):
	a ={}
	for item in alphabet:
		a[item] = 0
	return a

# main function to generate possible worlds give an alphabet (a..z)

def generatePossibleWorlds(alphabet):

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
	initialRow =  generateIntialRow(alphabet)

	#add first possible world and find rest of possible worlds
	possibleWorldsTable.append(initialRow)
	for i in range (numPossibleWorld - 1):
		addNextRow(possibleWorldsTable, reverseAlphabet)

	#returns a list of possible worlds
	#possible worlds represented as dictionary
	return possibleWorldsTable

#print 'possible worlds:', generatePossibleWorlds(['a', 'b'])







