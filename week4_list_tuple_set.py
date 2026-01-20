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
Q = [0:-1]
print(Q)
# ==============================================================
