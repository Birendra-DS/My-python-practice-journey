# =========================================================
""" 🟦 QUESTION — Remove the Last Element Using Slicing
Problem Statement
You are given a non-empty list P containing n elements.
Your task is to create a new list Q that contains:
    all elements of P except the last one
    You must use list slicing, not loops.

Input Format
n
p1 p2 p3 ... pn

Where:
n ≥ 1
the second line contains n space-separated values

Output Format
Print the list Q containing the first n−1 elements of P.

Example
Input
5
10 20 30 40 50

Output
[10, 20, 30, 40]
Rules (IMPORTANT)

You must:
create a new list using slicing
not modify the original list
not use loops

You may use any valid slicing form, such as:
start and end index
negative indexing
omitted start index
Allowed Examples of Slicing

All of the following are valid:
P[0:len(P)-1]
P[:len(P)-1]
P[0:-1]
P[:-1]

Your program may use any one of them."""

'''
n = int(input())
# split() separates by spaces result is list of strings
# convert string to integer
p = list(map(int,input().split()))
Q = p[0:-1]
print(Q)
'''

# ==============================================================
# 🟦 QUESTION — Print Squares of Numbers
"""
Problem Statement
You are given a list L containing positive integers.
Your task is to print the square of each number in the list, one value per line.

Input Format
n
L1 L2 L3 ... Ln

Where:
n is the number of elements
the second line contains n space-separated integers

Output Format
Print the square of each number in the list, one per line, in the same order.

Example
Input
5
1 2 3 4 5

Output
1
4
9
16
25

Rules (IMPORTANT)
You may use:
for x in L
OR for i in range(len(L))
You must:
square the values, not the indices
print exactly one number per line

Do NOT:
modify the list
use list comprehensions
pre-store squared values unless required"""\
'''
number = list(map(int,input().split())) # store list of values and take input many numbers

for x in number:       # loop over all list element
    print(x**2)
'''

# =============================================

""" 🟦 QUESTION — Filter Even Numbers from a List
Problem Statement
You are given a list of integers named nums.

Your task is to:
filter all even numbers
preserve their original order
store them in a new list called even_nums
finally, print the list even_nums

Input Format
n
num1 num2 num3 ... numn

Where:
n is the number of elements
the second line contains n space-separated integers
Output Format
Print the list even_nums.

Example
Input

6
3 4 7 10 11 8

Output
[4, 10, 8]

Rules (IMPORTANT)
You must:
use a loop
check values, not indices
append only even numbers

Do NOT:
use list comprehensions
use slicing
modify the original list"""

'''
num = list(map(int,input("Enter number:").split()))
even_lst = []           # store all even number

for i in num:
    if i % 2 == 0:      # filter all odd number
        even_lst.append(i)
print(even_lst)
'''

#====================================================
""" 
You are given a list representing a user's shopping cart.
Each number represents the price of an item.

🧾 Input
n
price1 price2 price3 ... pricen
discount

Where:
n = number of items

prices are integers
discount is an integer percentage

🧪 Example Input
5
100 200 300 400 500
10

🎯 Requirements

You must:
    Store the original cart in a list named cart
    Create another list named discount_cart
    Apply discount only on discount_cart

Print:

Original Cart:
<cart>

Discounted Cart:
<discount_cart>

✅ Discount rule

If discount = 10:
new_price = price - (price * discount / 100)


Convert final prices to integers.
❗ IMPORTANT RULES (very important)
❌ You must NOT modify cart
❌ You must NOT use slicing like cart[:]
❌ You must NOT use .copy()
❌ You must NOT use list()

If you use:
discount_cart = cart
Your solution is wrong, even if output looks correct.

⚠️ Why this problem exists
    This problem tests whether you understand:
    list mutability
    aliasing
    independent memory objects
    side effects

This exact bug appears in:
    Django projects
    backend APIs
    data pipelines
    analytics preprocessing
"""
'''
cart = list(map(int,input("Enter prices:").split()))
disc = int(input("Enter the discount:"))

# creating different memory location 
discount_cart = []
for price in cart:
    discount_cart.append(price)

disc_cart_price = []
for x in discount_cart:
    new_price = int(x - (x * disc / 100))       # convert price to integer
    disc_cart_price.append(new_price)
print(disc_cart_price)
print(discount_cart)        # # discount_cart refers to a different list object in memory
print(cart)                 # cart remains unchanged because both lists are independent
'''
# ====================================================
    # shallow copy and  nested list problem
A = [[1, 2], [3, 4]]
B = A.copy()
A[1][1] = 100           # it change both A and B
A.append(20)            # it change only A not B beause B is shallow copy of A

print(A)
print(B)
# =======================================================
# Divisibility Check (Boolean Output)
"""
Problem Statement
You are given an integer n.
Your task is to determine whether n is divisible by 5.
Input Format
n

Output Format

Print:
True
if n is divisible by 5, otherwise print:
False

Example 1
Input
25

Output
True

Example 2
Input
13

Output
False
Rules (IMPORTANT)

You may use:
if–else
OR direct boolean expression
OR conditional (ternary) expression
Output must be exactly True or False
Do not print extra text
"""
'''
def check_divisiblity_by_5(n):
    """ check divisibility by five"""
    if n % 5 == 0:
        print(True)
    else:
        print(False)

n = int(input("Enter number:"))
(check_divisiblity_by_5(n))

""" or even simple and more pythonic way is """
print(n%5==0)           # Comparisons already return True or False.
"""
'''
# ===============================================
# Problem- Even Numbers Using List Comprehension
"""
Problem Statement
You are given an integer n.
Your task is to create a list that contains all even numbers from 0 to n − 1.
You must use list comprehension.

Input Format
n

Output Format
Print the list of even numbers.

Example
Input
10

Output
[0, 2, 4, 6, 8]

Rules (IMPORTANT)
You must use list comprehension

You must include:
an iteration (for)
a condition (if)

Do NOT:
use a normal loop with append
print values one by one
Required Syntax Pattern
[expression for item in iterable if condition]"""

"""
print("List comprehension of even number problem")
n = int(input())
even_num_lst = [num for num in range(n) if num % 2 == 0]
print(even_num_lst)
"""
# ========================================================
#  PROBLEM — Filter Words by First and Last Letter
"""
Problem Statement
You are given a list of words L.
Your task is to create a new list P that contains only those words which:
begin with the same letter they end with

Input Format
n
word1 word2 word3 ... wordn

Where:
n is the number of words
all words are lowercase strings without space
Output Format
Print the list P.

Example
Input
6
level radar apple civic python noon

Output
['level', 'radar', 'civic', 'noon']

Rules (IMPORTANT)
You may solve using:
list comprehension
OR a normal loop

You must:
check the first character
check the last character
compare them

Do NOT:
use string slicing like word[::-1]
reverse the string
use external libraries"""

print("First and last element matching problem")
L = ['level', 'radar', 'civic', 'noon']
p = []          # store the result words
for word in L:
    # check first and last element
    if word[0] == word[-1]:
        p.append(word)
print(p)

# or using list comprehension method
p_lst = [word for word in L if word[0] == word[-1]]
print(p_lst)

# ==============================================================
# 🟦 CODING PROBLEM — Pairs with Sum Equal to 100
"""
Problem Statement
You are given an integer S (sum value).
Your task is to generate all pairs (x, y) such that:
x + y = S
x > 0
y > 0
Store all valid pairs as tuples inside a list.

Input Format
S

Output Format
Print a list of tuples:
[(x1, y1), (x2, y2), ...]

Example
Input
100

Output
[(1, 99), (2, 98), (3, 97), ..., (99, 1)]

Rules (IMPORTANT)
You may solve this problem in any one of the following ways:
nested loops
nested list comprehension
optimized single-loop logic

But you must follow all constraints.
Constraints
1 ≤ x < S
y = S − x
both values must be positive

Efficiency Requirement
After solving it once, try to answer:
Can this be solved without checking all pairs?
This question separates average students from strong programmers."""

s = 100
rslt = []
for x in range(1,s):    # range is from 1 to not include 0
    for y in range(1,s):
        if x + y == s:
            rslt.append((x,y))
print(rslt)

print("\nFastest method)\n")
final = []
for x in range(1,s):
    final.append((x, s-x))
print(final)

# ==============================================
# PROBLEM — Pairs with Sum = S and Constraint (x ≤ y)
""" 
Problem Statement
You are given an integer S.
Your task is to generate all pairs (x, y) such that:
x + y = S
x > 0
y > 0
x ≤ y
Store all valid pairs as tuples inside a list.

Input Format
S

Output Format
Print a list of tuples:
[(x1, y1), (x2, y2), ...]

Example
Input
100

Output
[(1, 99), (2, 98), (3, 97), ..., (50, 50)]
Explanation (conceptual only)
Pairs like (60, 40) are not allowed
because x > y
Pairs like (40, 60) are allowed
(50, 50) is valid because x ≤ y
Rules (IMPORTANT)

You may solve this problem using:
nested loops
nested list comprehension
optimized single-loop logic

But your solution must:
include the condition x ≤ y
not generate duplicate mirror pairs"""
print("2nd part")
sm = 100
rl = []
for x in range(1,sm):
    y = sm-x            # y is directly calculated using x value without looping again
    if x <= y and x + y == sm:
        rl.append((x,y))
print(rl)
# ===================================================================

"""
PROBLEM — Create a Matrix of Zeros
Problem Statement

You are given two integers:
rows
cols

Your task is to create a 2-D matrix with:
rows number of rows
cols number of columns
Every element of the matrix must be 0.

Input Format
rows cols
Output Format
Print the matrix as a list of lists.

Example
Input
3 3

Output
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Rules (IMPORTANT)

You must:
use nested loops
create a new inner list for each row
append values manually
You must NOT use

❌ list comprehension
❌ multiplication like [[0]*cols]*rows
❌ numpy
❌ external libraries

(These cause aliasing bugs.)
Key Requirement
Each row must be an independent list object.
"""
rw = int(input("Enter rows:"))
cl = int(input("Enter columns:"))
mat = []                # this will store rows

for i in range(rw):     # this loop runs once per row
    # for each row create a new list
    row = []            # new inner list
    # each row must have col elemnts
    for j in range(cl):
        row.append(0)   # fill that row with zeroes
    # Add that row to matrix
    mat.append(row)

print(mat)
#===========================================
# Problem - Word Frequency Counter
"""
(Dictionary Comprehension Practice)

🧠 Problem Statement
You are given a list of words.
Your task is to create a dictionary that stores:
each unique word as a key
the number of times that word appears in the list as its value

📥 Input
A list of strings:
L = ['one', 'two', 'one', 'three', 'one']

📤 Output
A dictionary showing frequency of each word:
{'one': 3, 'two': 1, 'three': 1}

✅ Rules
You must:
use dictionary comprehension
count how many times each word appears
store the result in a dictionary named freq

You may use:
list.count()
comprehension syntax

Do NOT:
manually create keys
write multiple loops
hardcode values"""

L = ['one', 'two', 'one', 'three', 'one']
freq = {}

for word in L:
    #word = word.count(word)
    freq[word] = L.count(word)

print(freq)

L = ['one', 'two', 'one', 'three', 'one']
freq = {}
    # Method 2: 
for wrd in L:
    if wrd in freq:
        freq[wrd] += 1
    else:
        freq[wrd] = 1
# count word frequency in single pass (O(n))
print(freq)

#=================================================
# Dictionary Key–Value Reversal
"""
🧠 Problem Statement
You are given a dictionary P where:
keys are strings
values are unique integers
Your task is to reverse the dictionary, meaning:
dictionary keys become values
dictionary values become keys

📥 Input
A dictionary:
P = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4
}

📤 Output
A reversed dictionary:
{
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four'
}
✅ Requirements

You must:
use dictionary comprehension
iterate through the dictionary
reverse key–value pairs

❌ Do NOT
hardcode the output
manually type the reversed dictionary
use external libraries"""

P_org = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4
}
p_rev = {}
for key, value in P_org.items():    # .items() return both key and value pairs as  tuple format
    p_rev[value] = key

print(p_rev)

   

#print(p_r)
