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





# ======================================================
