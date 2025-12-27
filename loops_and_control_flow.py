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
def mult_table(n = int(input("Enter a no:"))):
    for i in range(1,11):
        print(n*i)

mult_table()