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

    # If you initialize with the first element,
    # your loop must run n-1 times, not n times.
    while odd_counter < x:
        first_odd += 2
        odd_counter += 1
        odd_sum += first_odd               

    return odd_sum


# same code using for loop
def get_sum_of_odd(x):
    current_odd = 1
    odd_sum = 0

    # for loop is professional here because we know quanitity 
    for _ in range(x):
        odd_sum += current_odd
        current_odd += 2

    return odd_sum 


n = int(input())
print("sum of odd:", get_first_n_odd(n))
print("Sum of odd using for loop:", get_sum_of_odd(n))





# ======================================================
# 🧠 Problem: Batch Login Attempt Analyzer
""" 
Context (realistic scenario)
You are given multiple users.
For each user, the system allows up to 3 login attempts.
If the user enters the correct password, stop attempts for that user.
If the user fails 3 times, lock the account and move to the next user.

Input Format
An integer n → number of users

For each user:
A string correct_password
Then multiple strings representing attempted passwords (user input simulation)
You should simulate this using input.

Rules
For each user:
Allow maximum 3 attempts
If password matches → print "Login successful"
If 3 attempts fail → print "Account locked"

Output Format
For each user, print one line:
"Login successful"
OR
"Account locked"

Example (just for understanding, not exact input)
Input:
2
abc123
wrong
123
abc123
pass
pass
pass

Output:
Login successful
Account locked

Constraints
You must use:
for loop → to iterate over users
while loop → to handle retry attempts per user
No shortcuts. No tricks."""

n = int(input("Enter number of users:"))    
correct_password = "Bir" 

# Use user_index to show it is number: 0, 1, 2 -> n
for user_index in range(n):           # iterate thorugh each user till the range n
    attempt_count = 0
    print("\n⏭️ Next user chance")
    print(f"User {user_index + 1} enter password:")     # user_index + 1 give actual user number(0->1, 1->2 etc)

    while attempt_count < 3:
        attempted_pass = input("Enter the password:")
        attempt_count += 1
    
        if attempted_pass == correct_password:
            print("Login successful")
            # without break it continue even if usertype correct password
            break                       # terminate the while loop.

        else:
            if attempt_count == 3:
                print("Account locked")
                
            else: 
                print("❌Wrong password try again")



# =======================================================================
# 🟦 QUESTION — Nested Loop Equivalence (While Version)
"""
Problem Statement
You are given the following nested loop logic in conceptual form:

For every value of x from 0 to 99,
and for every value of y from 0 to 99,
print the pair (x, y) only if x is not equal to y.

Your task is to implement this logic using ONLY while loops.

Rules & Constraints
You must use:
two while loops (nested)
no for loops

You must:
correctly initialize both loop variables
correctly reset the inner loop variable each time the outer loop runs
Do not print (x, x) pairs.

Output Format
Each valid pair should be printed in this format:
x y
(one pair per line)

Expected Behavior (Important)
Your program should print:
0 1
0 2
...
0 99
1 0
1 2
...
1 99
...
98 0
98 1
...
98 99
99 0
99 1
...
99 98

But never:
0 0
1 1
2 2
...
99 99

Input Format
No input.

🚫 What you are NOT allowed to do
❌ Do not use for
❌ Do not hardcode values
❌ Do not skip resetting y
❌ Do not print x 
"""

'''x = 0
while x < 100:      # process each x values
    y = 0           # reset y for each x
    while y < 100:   # process each y values
        if x!= y:       
            print(x,y)
        y = y+1         # move to next y value
    x = x+1             # move to next x value'''

# ======================================================================
# 🟦 QUESTION — Average Coins from String
"""
Problem Statement
You are given a string that represents boxes of coins.
The string format is like:
|1|4|1|5|9|
The vertical bar | is a separator.
Each number between two bars represents the number of coins in one box.
All numbers are single-digit non-negative integers.

Your task is to calculate the average number of coins per box.

Input Format
A single line containing the string:
boxes

Example:
|1|4|1|5|9|

Output Format
Print a single floating-point number — the average number of coins.

Rules
You must:
iterate over the string
ignore the | characters
convert digit characters to integers
count how many boxes are present
compute the average

Do not use:
split()
regex
external libraries
Use only loops, conditions, and type conversion.

Example
Input
|1|4|1|5|9|

Output
4.0
(Explanation: (1 + 4 + 1 + 5 + 9) / 5 = 4.0)

Important Notes (read carefully)
The string will always start and end with |
There will be no spaces
Every box contains exactly one digit
"""

def get_avg(boxes):
    total = 0               # store sum of coins
    count = 0               # store number of boxes

    for  char in boxes :
        if char != "|":             
            digit = int(char)           # convert character into integer 
            total += digit
            count = count +1             # keep count of integer value
    # avg need final total and count. So we only get these after the loop finish
    avg = total / count
    return avg

    

boxes = "|3|0|2|"
print(get_avg(boxes))


