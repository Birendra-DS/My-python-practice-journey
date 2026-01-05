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
#def mult_table():
 #   for i in range(1,11):
        #print(n*i)
        
#n = int(input("Enter a no:"))
#mult_table()
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

#n = int(input("Please enter a no:"))
#get_factor(n)

# Note: Printing is for humans.Returning is for programs.
        #Jobs want programs, not print statements.
        # so again write using return
def get_True_factor(n:int)->list[int]:
    factor = []
    for i in range(1,n+1):
        if n%i == 0:
            factor.append(i)
    return factor

#n = int(input("Please enter a no:"))
#print(get_True_factor(n))

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
for i in range(1,11):
        # print first 10 even number 
        print(i*2)

# write using function — same questions
def get_first_n_even(n:int)-> None:
    for i in range(1,n+1):
        print(i*2)

#n = int(input("Enter the number whose first even no. you want to get:"))
#get_first_n_even(n)


# =====================================================
""" 🟩 QUESTION 4 — Square Printer
Problem Statement
Print the square of numbers from 1 to 5 in the following format:
The square of X is equal to Y

Input Format
No input.

Output Format
Exactly 5 lines.

Example Output
The square of 1 is equal to 1
The square of 2 is equal to 4
The square of 3 is equal to 9
The square of 4 is equal to 16
The square of 5 is equal to 25
"""
for i in range(1,6):
    print("The square of", i, "is equal to", i**2)
    
# Function version
def sqr_printer(n):
    for i in range(1,n+1):
        print(f"The square of {i} is equal to {i**2}")

#n = int(input("Enter a number n to print square from 1 to n:"))
#sqr_printer(n)

# ======================================================================
# while loop concepts
"""
year = int(input("When did India get indepenedent. Type only its year:"))
if year == 1947:
    print("Congratulations, You got it")
else:
    print("Alas, you don't even know this")
    print("Ok lets I give you one more chance")
    year = int(input("please try again:"))
    if year == 1947:
        print("COngratuations. Your mind remember the year")
    else:
        print("Chee")
        print("One last chance.try again")
        year = int(input("Enter the year:"))
        if year == 1947:
            print("COngratuations. Your mind remember the year")
        else:
            print("Shame on you")
        # You can see that how hard it is using only if else method. But while loop can do it easily and in less line of code

# same problem using while loop
year = int(input("when did India got independence:"))
# it loops until you type 1947.
while(year != 1947):
    print("❌👎. Please try again. I will not allow you to come outside the dangerous(while) loop until you don't give correct year")
    year = int(input("Type the correct answer:"))
print("🙏Hurray. You got it. Now you are free from the loop")
"""

""" 🟩 QUESTION 5 — Loop Until Multiple
Problem Statement
Keep reading integers until the number entered is a multiple of 5 or 10.
Then print that number and stop.

Input Format
Multiple integers (one per line).

Output Format
Print the terminating number.

Example
Input
7
9
11
20

Output
20
"""
def check_mult_of_five(n):
    # it become false when n is multiple of 5, otherwise it ask for valid input.
    while n % 5 != 0:
        n = int(input("Try again.Enter a number:"))
    return n

    
#x = int(input("Enter num mult of 5:"))
#print(check_mult_of_five(x))


# ==========================================================
"""Write a funtion to find the factorial of a given number"""
""" Pseudocode
 Start with result = 1
 Start with counter = n
 While counter is greater than 0
 Multiply result by counter
 Decrease counter by 1"""

# Using function
def get_factorial(n:int)-> int:
    if n < 0:
        raise ValueError("Invalid Input:Factorial is not defined for negative number")
        
    result = 1
    counter = n
            
    while counter > 0:
        result = result * counter
        counter = counter - 1
    return result


print(get_factorial(2))
# =================================================
""" 🟢 Problem 1 — Sum of Digits (Accumulator mastery)
Problem
Write a program that:
takes a positive integer
calculates the sum of its digits

Example
Input: 472
Output: 13   (4 + 7 + 2)
"""

    # Pseudocode
"""
1️⃣ Take a positive integer from the user
2️⃣ Store it in a variable called num
3️⃣ Initialize sum = 0
4️⃣ While num is greater than 0
5️⃣ Extract the last digit using % 10
6️⃣ Add the extracted digit to sum
7️⃣ Remove the last digit from num using // 10
8️⃣ Loop stops automatically when num becomes 0
"""
def get_sum_digits(n):
    num = n
    if num < 0:
        raise ValueError("Please give positive number")
    
    # do not use sum as a variable name as it is build in python function
    digit_sum = 0         # It is use to store the final result

    # Condition n> 0 become False as soon as num hit zero
    while num > 0:
        extract_dig = num % 10                  # get the last digit
        digit_sum = digit_sum + extract_dig     # add the last digit to the digit_sum
        num = num // 10                         # remove digits from the num to make condition false 

    return digit_sum


#x = int(input("Enter the number to get the sum:"))
#print(f"sum of the digit is {get_sum_digits(x)}")

# ================================================================
# 🔵 PROBLEM  — Reverse a Number
""" 
Goal 
Given a positive integer, produce a new number with digits reversed.

Example:
Input: 1234
Output: 4321"""

    # Pseudocode
"""
1. Take input from users(positive)
2. Store that number in new variable called num
3. Define reverse variable to store  the final result
4. while the number greater than 0
    5. Multiply last digit by 10 to shift the reverse left
    6. Extract the last digit and add it to reverse variable
    7. remove digits from num to make condition False
8. return the reverse digit """

def rev_digit(x):
    num = x 
    rev_num = 0

    while num > 0:
        # rev_num = rev_num * 10--> we can also write this after extracted_dig line 
        extracted_dig = num % 10
        rev_num = rev_num * 10 + extracted_dig      # shift the reverse left and add the extracted digit
        num = num // 10     # it makes condition false

    return rev_num


# =================================================
""" 🟩 QUESTION 6 — Smallest Divisible Expression
Problem Statement
Using a while loop, find the smallest positive integer x such that:
x² + x + 41
is divisible by 41.

Input Format
No input.

Output Format
Print the value of x.
"""
    # Pseudocode
"""
Start with the smallest positive integer
Repeat while the expression is not divisible by 41
    Compute the expression using the current value
    Move to the next value
Stop when the expression becomes divisible by 41
Output the value
""" 
x = 1                           # starts with the smallest positive integer
num = x**2 + x + 41             # current value of the expression 
while num % 41 != 0:            # keep seaching untill the expresion become divisible
    x = x + 1                   # try the next integer
    num =  x**2 + x + 41       # Recompute num for the new x
print(x)

# =======================================
""" Average of First 50 Odd Numbers
Problem Statement
Calculate the average of the first 50 odd positive integers.

Input Format
No input.

Output Format
Print the average (as a float).
"""
""" Approach
1.) Calculate the first 50 odd positive integer
2) Sum all 50 odd positive integer and divide it by 50
3) 1, 3, 5,7,9,11,
4) If n % 2 != 0: 
"""

"""Pseudocode
1.) set variable to the first odd number
2.) set count 0 to track number of odd number
3.) set sum 0 to get the total sum of odds
4.) while count less than 50
    5.) Increment the count vriable by 2
    6.) Add count varible to first odd
    7.) Add them to the sum
8.) Get sum
9.) Average is sum divided by 50"""

first_odd = 1       # First odd number from starts
count_odd = 1       # counts how many odds number are included
odd_sum = 1         # track odd number sum so far

while count_odd < 50:       # loop untill 50 odd number are counted
    first_odd = first_odd + 2           # Add 2 to get another odd number
    count_odd = count_odd + 1           # Tracks the count of odd number
    odd_sum = odd_sum + first_odd       # add current odd number to the sum

print("Sum of 1st 50 odd is:",odd_sum)
average = odd_sum / 50
print("Average of 1st 50 odd:", average)




# =========================================================
""" 🟩 QUESTION 8 — Nested Loop Sum
Problem Statement
Compute the value of total after executing the following logic:

total = 0
for i from 1 to 4:
    repeat i times:
        total += i

Input Format
No input.

Output Format
Print the final value of total."""

""" Pseudocode
1.) set total to zero
2.) for each number from 1 to 4
    3.) multiply each number by itself and then add to the total
    4.) print total value 
"""
total = 0 
for i in range(1,5):
    i = i * i               # repeating each value ❌
    total = total + i       # additing each repeating number to the total
    print(i)
print ("Total:", total)


total = 0
for i in range(1,5):
    rep_counter = 1         # starts counting repetition from 1

    while rep_counter <= i: # Runs exactly i times
        total += i          # Add i once per repition
        rep_counter += 1   # Ensures the loop terminate. Move to the next repetition

print("Final total:", total)

# =========================================================
"""— Asterisk Counter

Problem Statement
Print a pattern where line i contains i asterisks (*) for i from 0 to 99.

Then print the total number of asterisks printed.

Input Format
No input.

Output Format
Print a single integer — total count of *."""
total = 0
for i in range(0,100):
    stars = i*"*"
    total = total + i   
    #print(stars)                       # shows patterns
print("Total count of * is",total)

# ===============================================================
""" 🟩 QUESTION 10 — Break Counter
Problem Statement
Given the following logic:

for i in range(10):
    for j in range(10):
        break
    break

Count:
How many times the inner break executes
How many times the outer break executes

Input Format
No input.

Output Format
Print two integers on separate lines:

inner_break_count
outer_break_count
"""

# ==========================================================
""" 🟩 QUESTION 11 — Float Formatter
Problem Statement
You are given a floating-point number x.
Print it rounded to exactly two decimal places.

Input Format
x

Output Format
formatted_value

Example
Input
1234.2

Output
1234.20
"""
def round_float(n):
    return f" {n:.2f}"

# n competitive programming / exams:❌ prompts are not allowed
#   ✅ plain input() is expected
n = float(input())
print(round_float(n))