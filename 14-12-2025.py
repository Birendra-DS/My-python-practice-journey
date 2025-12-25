# ===============================================================
# Q1. Which of the following are valid variable names in Python?
# a_, _a, 1a, a variable, a_variable
    # My thinking:
        # - Python variables cannot start with a number
        # - They cannot contain spaces
        # - They can start with underscore
a_ = 2
_a = 2

print(_a)
print(a_)

# Uncommenting below lines will cause errors:
    # 1a = 5
    # a variable = 6
# ========================================================

# =========================================================
# ==================================================
# PROBLEM 2: Swap and Compare Strings (YOU DO THIS)
# ==================================================
# Problem Statement:
# Given two strings word1 and word2:
# 1. Print word1 + word2
# 2. Swap the strings using a temporary variable
# 3. Print word2 + word1
# 4. Print True if both outputs are same, else False
#
# Input: two strings
# Output: three lines

# Observstion:
    #1. Both print statement are only same when both word_1 == word_2
    # we can use a third variable to swap the value of the variable easily

# Same code using function
def swap(word_1, word_2):
    L1 = word_1 + word_2
    # using the three assignment
    word = word_1
    word_1 = word_2
    word_2 = word
    L2 = word_1 + word_2     # Now word_1 = Elon nad word_2 = Hello
    return L1, L2

# ======================================================
"""🟦 QUESTION 3 — Chained Assignment Result
Problem Statement
You are given three distinct integers a, b, and c.
Perform the following operations in order:
Assign a, b, c to variables x, y, z respectively.
Then assign the value of z to all three variables using chained assignment.
Finally, print the values of x, y, and z

Imput format: a b c (Three-spaced seperated integers)
output: x y z (three spaced separated integer all eqaul to z)

Example: 
Input: 4 7 8
output: 8 8 8

"""
def chaining(a,b,c):
    x = a
    y = b
    z = c
    x = y = z       # assign z's value to all
    return x,y,z

print(chaining(4,7,8))
    # but here we copy a,b,c first
    # why do we copy a,b,c first if we throw away it at the end?
        # so we need a better version to not do redundant work

# ======================================================
"""🟦 QUESTION 4 — Integer Casting with Negatives
Problem Statement
You are given a floating-point number x.

Print:
The integer value obtained by converting x to an integer.
The integer value obtained by converting -x to an integer.

Input Format
A single floating-point number:x

Output Format
Print two lines:
int(x)
int(-x)

Example
Input: 3.75
Output: 
3
-3
"""

def flt_num(x):
    return int(x), int(-x)

x = 3.75
print(flt_num((x)))      # it gives answer in tuple format
pos_val,neg_val = flt_num(x)        # unpacking the output from tuble so that we return in next line
print(pos_val)
print(neg_val)
# ====================================================================

""" 🟦 QUESTION 5 — Boolean Shortcut Check
Problem Statement
You are given a boolean value flag.

If flag is True, print:
works
Otherwise, print nothing.

⚠️ You must use only:
if flag:
Input Format

A string that is either:
True
or
False

Output Format
Print:
works

(if applicable)

Example
Input: True
Output: works
"""

def check_bool(flag):
    if flag:
        print("works")
    
s = input().strip()  
flag = (s == "True")
(check_bool(flag))

# ==============================================================
""" 🟦 QUESTION 6 — Safe Variable Printing
Problem Statement
You are given three boolean values E1, E2, and E3.
Execute the following logic:

if E1:
    x = 1
if E2:
    x = 2
if E3:
    x = 3
print(x)

If printing x causes an error (because it was never defined), print:
Error
Otherwise, print the value of x.

Input Format
Three lines:
E1
E2
E3
(each is True or False)

Output Format
Print either:
x
or
Error

Example:
    Input
        False
        False
        False

Output
Error"""

def bool_val(E1,E2,E3):     # E1, E2, E3 contain boolean value 
    x = None        # Lets assume x doesn't contain anything initially/ x is empty(better comment)

    if E1:
        x = 1
    if E2:
        x = 2
    if E3:
        x = 3

    if x is None:      # if x in None it means E1,E2,E3 contain False bool value
        print("Error")
    else:               # print final x value
        print(x)
    
bool_val(False, True, False)
# =============================================================
"""🟦 QUESTION 7 — Print a Backslash
Problem Statement
Print a single backslash character (\) to the output.

Input Format
No input.

Output Format: \
"""
print("\\")     # Double backlash is use to print single backslash
# ===================================================
"""
🟦 QUESTION 8 — Name Validator
Problem Statement
You are given a string name.

A name is valid if:
It contains only alphabets
It contains no spaces

Print:
Valid
or
Invalid

Input Format
A single string:
name

Example
Input: Rohit
Output: Valid
"""
def check_valid_name(name):
    if name.isalpha():
        print("Valid")
    else:
        print("invalid")

n = "Rohit"
check_valid_name(n)
    