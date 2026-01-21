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

n = int(input())
# split() separates by spaces result is list of strings
# convert string to integer
p = list(map(int,input().split()))
Q = p[0:-1]
print(Q)
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
pre-store squared values unless required"""

number = list(map(int,input().split())) # store list of values and take input many numbers

for x in number:       # loop over all list element
    print(x**2)

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

num = list(map(int,input("Enter number:").split()))
even_lst = []           # store all even number

for i in num:
    if i % 2 == 0:      # filter all odd number
        even_lst.append(i)
print(even_lst)

