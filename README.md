# pl-basic-toolkit
Some tools for propositional logic that includes a wff checker, a parse tree builder and a model builder. 

There are 5 files:

1) parser.py
2) ttable.py (depends on parser.py and worlds.py)
3) wff.py
4) worlds.py
5) starter.py (depends on parser.py and ttable.py)

The wff.py file checks if a sentence is a valid wff.

The parser.py file is the same as the wff.py file but also builds a parse tree of the
sentence.

The worlds.py generates the possible worlds given the alphabet of the language.

The ttable.py builds the truth table given a parse tree and the set of possible worlds.

Note: The wff.py is redundant as its functionlaity is covered by parser.py.

-----------------------------------------------------------------------------

Start with the starter.py.

Just execute it normally as you would a python file.
You will be prompted to enter a sentence.
 
Try (a -> b) for example. 

If the sentence you entered is not a valid wff of propositional logic, it will
give you a message saying so. 

If it is a valid formula, it will produce the truth table of that formula.
