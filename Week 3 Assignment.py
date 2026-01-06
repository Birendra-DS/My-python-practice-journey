# ===============================================================
    # Question 1: Max Power of 2 
""" 
Problem:
Write a program that accepts a positive integer x as input and prints the maximum value of the integer y such that 2^y <= x.

Sample Test Cases:
Input: 100 -> Output: 6
Input: 256 -> Output: 8
 """
"""Pseudocode
1) Read the integer x
2) Take y = 0
3) while x is greater than or equal to 2
    4) divide x by 2
    5) increase y by 1
6) print y

 """
x = int(input("Enter the integer:"))
y = 0               # It keep keep count of the power
while x > 2:        # ⁉️ why not x> 1?
    x = x // 2      # x // 2 performs integer (floor) division. ⁉️ why not we do x / 2 (float division)
    y = y + 1
print(y)

# ===============================================================
    #  Question 3: Sum of First n Odd Numbers (While Loop)
"""
Problem: write a code that prints the sum of the first n odd numbers starting from 1 (including).
Assume n is a positive integer and is already defined. 
Example: n = 5 ,
output: 1+3+5+7+9 = 25
 """
"""Pseudocode
1) get the input x from the user
2) keep first odd equal to 1
3) keep odd counter equal to 1 
4) keep sum of odd equal to 1
5_ while odd counter less than or equal to x
    6) increase +2 to first odd 
    7) increase odd ocunter by 1
    8) add first odd value to  sum of odds
9) print the sum of odds
"""
def get_first_n_odd(x):
    first_odd = 1
    odd_sum = 1
    odd_counter = 1
    while odd_counter <= x:
        first_odd += 2
        odd_counter += 1
        odd_sum += first_odd                

    return odd_sum

n = int(input())
print("sum of odd:", get_first_n_odd(n))

