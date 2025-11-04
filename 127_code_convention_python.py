#TABS: Tabs are very important in python

#GOOD
def my_function1():
    x = []

    if x:
        print("Hello, World!")


#BAD
def my_function():
 x = []
 if x:
  print("Hello, world!")



#Maximum Line Length: Limit lines to 79 characters for code and 72
#  for docstrings and comments. However, the more modern recommendation
#  is to limit lines to 88 characters, as it works well with modern text editors and widescreen displays.



# Good
def long_function_name1(parameter1, parameter2, parameter3,
                       parameter4, parameter5):
   print("HI")
    # Code goes here...

# Bad (exceeds line length limit)
def long_function_name(parameter1, parameter2, parameter3, parameter4, parameter5):
    # Code goes here...
    print("hi")



#Imports: Imports should usually be on separate lines and grouped in the following order:

# Standard library imports
# Related third-party imports
# Local application/library specific imports


# Good
import os
import sys

from my_module import my_function

# Bad (unorganized or multiple imports on one line)
import os, sys
from my_module import *




#Whitespace in Expressions and Statements: Avoid extraneous whitespace in the following situations:

# Avoid whitespace immediately before a comma, semicolon, or colon.
# Avoid whitespace immediately before an open parenthesis that starts an argument list, indexing, or slicing.
# Avoid whitespace immediately before the open parenthesis that starts a function call.
# Avoid whitespace immediately before the open parenthesis that starts an indexing or slicing.



# Good
spam(ham[1], {eggs: 2})

# Bad (extraneous whitespace)
spam( ham[ 1 ], { eggs: 2 } )







#Comments: Use comments sparingly and focus on explaining why something is done,
#  not what it does (unless it’s particularly complex). Use docstrings to document classes, functions, and modules.




# Good:

def calculate_total1(price, tax_rate):

    """Calculate the total cost given a price and tax rate."""

    return price * (1 + tax_rate / 100)


# Bad (excessive or unclear comments):

def calculate_total(price, tax_rate):

    # This function calculates the total cost
    # Based on the given price and tax rate

    return price * (1 + tax_rate / 100)