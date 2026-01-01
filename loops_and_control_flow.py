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
for i in range(1,11):
        # print first 10 even number 
        print(i*2)

# write using function — same questions
def get_first_n_even(n:int)-> None:
    for i in range(1,n+1):
        print(i*2)

n = int(input("Enter the number whose first even no. you want to get:"))
get_first_n_even(n)


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

n = int(input("Enter a number n to print square from 1 to n:"))
sqr_printer(n)

# ======================================================================
# while loop concepts

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
n =  int(input("Enter any number:"))
while n % 5 != 0:
    n = int(input("Enter a number:"))
print(n)


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
        extract_dig = num % 10 
        digit_sum = digit_sum + extract_dig
        num = num // 10
    return digit_sum

x = int(input("Enter the number to get the sum:"))
print(f"sum of the digit is {get_sum_digits(x)}")

# ================================================================
# 🔵 PROBLEM 2 — Reverse a Number
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
        rev_num = rev_num * 10 + extracted_dig
        num = num // 10     # it make condition false
    return rev_num



        