""" 🟩 QUESTION 1 — Multiplication Table
Problem Statement

You are given an integer n.
Print the first 10 multiples of n, one on each line.

Input Format
n

Output Format

Print 10 lines:

n * 1
n * 2
...
n * 10

Example

Input

3


Output

3
6
9
12
15
18
21
24
27
30"""
# define n inside the parameter to take user input
def mult_table():
    for i in range(1,11):
        print(n*i)
        
n = int(input("Enter a no:"))
mult_table()
# =================================================

""" 🟩 QUESTION 2 — Print All Factors
Problem Statement
You are given a positive integer n.
Print all factors of n in increasing order, one per line.

Input Format
n
Output Format
Print all factors of n.

Example
Input
6

Output
1
2
3
6

for i in range:
    1,2,3,4,5,6
        if n%i== 0 
"""
def get_factor(n):
    # range should be from 1 so that it prevent zero division error and n+1 ensures that it include 6 also during factorising
    for i in range(1,n+1):
        # divide each n from i to get factor
        if n % i == 0:
            print(i)

n = int(input("Please enter a no:"))
get_factor(n)

# Note: Printing is for humans.Returning is for programs.
        #Jobs want programs, not print statements.
        # so again write using return
def get_True_factor(n:int)->list[int]:
    factor = []
    for i in range(1,n+1):
        if n%i == 0:
            factor.append(i)
    return factor

n = int(input("Please enter a no:"))
print(get_True_factor(n))

 # ====================================================

""" 🟩 QUESTION 3 — First 10 Even Numbers
Problem Statement
Print the first 10 positive even numbers, one per line.

Input Format
No input.

Output Format
2
4
6
...
20 
"""
for i in range(1,21):
    if i % 2 == 0:
        print(i)