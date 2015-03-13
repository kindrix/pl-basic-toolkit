# plBasicToolkit
Some tools for propositional logic that includes a wff checker, a parse tree builder and a model builder. 

-----------------------------------------------------------------------------
Content
-----------------------------------------------------------------------------

There are 5 files:

1) parser.py

2) ttable.py (depends on parser.py and worlds.py)

3) wff.py

4) worlds.py

5) starter.py (depends on parser.py and ttable.py)

- The wff.py file checks if a sentence is a valid wff.

- The parser.py file is the same as the wff.py file but also builds a parse tree of the
sentence.

- The worlds.py generates the possible worlds given the alphabet of the language.

- The ttable.py builds the truth table given a parse tree and the set of possible worlds.

- The starter.py file is just there to demonstrate how the other modules are to be used.

* Note: The wff.py is redundant as its functionlaity is covered by parser.py.

-----------------------------------------------------------------------------
Importing the package
-----------------------------------------------------------------------------


Usage:
	>>> import plBasicToolkit

	To use the modules, then call as follows:

	Parser:
		>>> plBasicToolkit.parse_wff(exp)

		The above example takes an string 'exp' and checks if it is a 
		valid wff and returns the parse tree. See 'parser' module for details

	Truth table builder

		>>> plBasicToolkit.get_truth_table(parseTree, alphabet)

		The  above example takes the parseTree (from parse_wff module above) along 
		with the alphabet of the language and returns the truth table. See documentation 
		'ttable' module for details. 

-----------------------------------------------------------------------------
Quick Start
-----------------------------------------------------------------------------
Download the zip file using the link in github. Unzip and navigate to the folder.

Start with the starter.py.

Just execute it normally as you would a python file.
You will be prompted to enter a sentence.
 
Enter '(a -> b)' without the quotes for example. 

If the sentence you entered is not a valid wff of propositional logic, it will
give you a message saying so. 

If it is a valid formula, it will produce the truth table of that formula.
