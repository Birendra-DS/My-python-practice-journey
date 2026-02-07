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

'''
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
'''
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

# =============================================
# Problem - — Dictionary of Prime Numbers
""" 
🧠 Problem Statement
You are given a range of integers from 2 to 100.
Your task is to create a dictionary where:
each number is a key
the value is a boolean indicating whether the number is prime

📥 Input
No user input.
The numbers are:
2 to 100 (inclusive)

📤 Output
A dictionary of the form:
{
    2: True,
    3: True,
    4: False,
    5: True,
    ...
    100: False
}
✅ Rules

You must:
write a function is_prime(n)
return True if n is prime
return False otherwise
generate a dictionary mapping numbers → prime status

❌ Do NOT
use any built-in prime libraries
hardcode answers
manually write each number"""

def is_prime(n):
   """return True if n is prime, otherwise False"""
   if n < 2:
       return False
   
   for i in range(2,n):
       if n % i == 0:       # check if n is divisible by any number from 2 to n-1
           return False
    # return True only after checking whole loop
   return True             # it is prime


prime = {}              # store prime number in bool value
for i in range(2,101):
    prime[i] = is_prime(i)

print(prime)

# By dictionary comprehendion method
prime_dict = {x: is_prime(x) for x in range(2,101)}
print(f"Dictionary Method {prime_dict}")

# ===========================================================
# Problem  — Function to Copy a List
"""
🧠 Problem Statement
You are given a list P.
Your task is to write a function named copy_list(P) that:
creates a new list
copies all elements of P into the new list
returns the copied list
The copied list must be independent of the original list.

📥 Input
A list P containing elements of any type.

Example:
P = [10, 20, 30, 40]

📤 Output
A new list containing the same elements:
[10, 20, 30, 40]

✅ Requirements

You must:
create an empty list Q
use a loop
copy elements one by one
return Q

❌ Do NOT
use list.copy()
use slicing (P[:])
use deepcopy
assign directly (Q = P)
"""
def copy_list(P):
    Q = []              # store copied element of list p
    for i in range(len((P))):
        Q.append(P[i])
    return Q

P = [10, 20, 30, 40]
print(copy_list(P))

# ======================================================
# Problem - Distance Function with Default Argument
"""
🧠 Problem Statement
You are asked to write a function named:
distance(x, y, metric)

The function calculates the distance of a point (x, y) from the origin (0, 0).

📌 Distance Metrics
1️⃣ Manhattan distance
|x| + |y|

2️⃣ Euclidean distance
√(x² + y²)

🎯 Task Requirements
The parameter metric must have a default value
If no metric is provided, the function must compute Manhattan distance
If metric is "euclidean", compute Euclidean distance
If metric is "manhattan", compute Manhattan distance

📥 Input Format
No user input required.
You must define and call the function in your code.

📤 Output Format
Print the returned distance value.

🧪 Example Calls
print(distance(3, 4))
print(distance(3, 4, "euclidean"))

Expected Output
7
5.0

Explanation:
distance(3, 4) → Manhattan → |3| + |4| = 7
distance(3, 4, "euclidean") → √(9 + 16) = 5

✅ Rules (IMPORTANT)
You must:
define the function correctly
place the default argument after non-default arguments
use conditional logic inside the function
return the computed value

❌ Do NOT
place default argument before non-default arguments
❌ def distance(metric='manhattan', x, y):
hardcode outputs
use external math libraries"""

def distance(x,y,metric = 'manhattan'):  # default matric is Manhattan
    """ Return distance of (x,y) from origin using given matric"""
    if metric == 'euclidean':
        # condition for euclidian: √(x^2 + y^2)
        return (x**2 + y**2)**0.5
    elif metric == "manhattan":
        # condition for manhattan matric: |x| + |y|
        return (abs(x)+abs(y))
    else:
        # raise ValueError("Invalid metric")    # This will stop further code execution too
        print("ValueError: Invalid metric")
    
print(distance(3,4,'euclidian'))

# =================================================
# Problem- Write a code to find the frequency of words appear and then find max word appear

def freq_of_word(text):
    # dictinary to store word with frequency
    freq = {}
    # split sentence into individual word
    words = text.split()
    # iterate through each word
    for word in words:
        if word in freq:
            freq[word] += 1         # increase count if word already exists
        else:                       
            freq[word] = 1          # add word with count 1

    # find the word with maximum frequency
    # key = freq.get means comparing is done using dictionary value, not using string ASCII value
    max_word = max(freq,key = freq.get)     # ⁉️ doubt in this
    
    return freq, max_word
    

text = "apple banana apple orange banana apple"
print(freq_of_word(text))

# =============================================
# Problem - Find two number that add up to target

""" # Test
numbers = [2, 7, 11, 15, 3, 6]
print(two_sum(numbers, 9))   # Output: (2, 7)
print(two_sum(numbers, 10))  # Output: (7, 3)
print(two_sum(numbers, 100)) # Output: None
def two_sum(numbers, target):
    Find two numbers that sum to target
"""
def two_sum(numbers, target):
    """
    Find two numbers that sum to target
    """
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i,j)
        
        return None

numbers = [2, 7, 11, 15, 3, 6]
print(two_sum(numbers, 9))


# Dictionary method
def two_sum_prb(numbs,target):
    seen = {}

    for num in range(len(numbs)):
        complement = target - numbs[num]
        if complement in seen:            
            return (complement, numbs[num])
        
        seen[numbs[num]] = 1

    return None
num = [2,3,2,4,2,1,7]
print(two_sum_prb(num, 9))



#========================================================
"""
MASTER CODING PROBLEM — Exploring Python Collections (Beginner-Friendly)
🧠 Problem Statement

You are given three collections:

a list of integers

a set of integers

a tuple of integers

Your task is to write a Python program that explores:

empty vs singleton collections

truthy vs falsy values

min, max, sum, length

sorting and reversing

indexing and slicing

membership checking

concatenation of iterables

This problem is designed to make you learn by writing code, not by reading theory.

📥 Given Data (Use exactly this)
int_iterable = [5, 2, 9, 1, 5]
some_collection = (10, 20, 30, 40, 50)
some_value = 30

some_iterable = [1, 2]
another_iterable = (3, 4)
yet_another_iterable = {5, 6}

string_iterable = ["apple", "banana", "cherry"]

🎯 Tasks (You must implement all of these)
1️⃣ Create basic collections

Create:

an empty list

an empty set

an empty tuple

Then create:

a singleton list

a singleton set

a singleton tuple

Print all of them.

2️⃣ Truthy vs falsy collections

Create:

one list that is falsy when passed to bool()

one tuple that is truthy

Print:

print(bool(your_list))
print(bool(your_tuple))

3️⃣ Basic aggregate operations

From int_iterable, compute and print:

minimum value

maximum value

sum of elements

length

sorted list (ascending)

sorted list (descending)

4️⃣ Reversing (only if possible)

Check whether int_iterable can be reversed using reversed().

If yes:

create a list of reversed elements

Otherwise:

sort ascending and then reverse

Print the result.

5️⃣ Indexing and slicing

From some_collection:

try to get the third last element

try to get elements at odd indices

If the operation is not possible, store None.

Print both results.

6️⃣ Membership test

Check whether some_value is present in some_collection.

Print True or False.

7️⃣ Membership in even indices (only if ordered)

If some_collection is ordered:

check whether some_value appears at an even index

Else:

print None

8️⃣ Concatenation of iterables

Combine:

some_iterable
another_iterable
yet_another_iterable


into one list and print it.

9️⃣ String concatenation

If string_iterable is ordered:

join all strings with "-" in between

Else:

sort first, then join

Print the final string.

❗ Rules (IMPORTANT)

You must:

use basic Python only

use loops and built-in functions (min, max, sum, len, sorted, reversed, bool)

not use advanced libraries

not skip any part"""


int_iterable = [5, 2, 9, 1, 5]
some_collection = (10, 20, 30, 40, 50)
some_value = 30

some_iterable = [1, 2]
another_iterable = (3, 4)
yet_another_iterable = {5, 6}

string_iterable = ["apple", "banana", "cherry"]

# Task 1: Empty vs Singleton Collections
emp_lst = []
emp_set = set()     # empty set
    # emp_set = {} -> this creates an empty dictionary
emp_tup = ()
sing_lst = [2]
sing_set = {2}
sing_tup = (2,)     # used the trailing comma for tuple. Without it, Python treats (2) as just int not tuple.

# printing all of these
print(emp_lst, type(emp_lst))
print(emp_set, type(emp_set))
print(emp_tup, type(emp_tup))

print(sing_lst, type(sing_lst))
print(sing_tup, type(sing_tup))
print(sing_set, type(sing_set))

# Task 2 Truty and Fasly
falsy_list = []
falsy_tup = ()
truthy_list = [2,3]
truthy_tup = (2,)

print(bool(falsy_list))       # it is falsy list: empty
print(bool(falsy_tup))        # it is falsy tuple: empty
print(bool(truthy_list))       # it is truthy list: contain element
print(bool(truthy_tup))         # it is truthy tuple contain element with comma

# Task 3 — Aggregates on int_iterable