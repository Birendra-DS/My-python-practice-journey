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
'''
x = int(input("Enter the integer:"))
y = 0               # It keep keep count of the power
while x > 2:        # ⁉️ why not x> 1?
    x = x // 2      # x // 2 performs integer (floor) division. ⁉️ why not we do x / 2 (float division)
    y = y + 1
print(y)
'''
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

'''
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
'''




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

'''
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

'''

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
'''
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
'''

# ==========================================================
"""🟦 QUESTION — Date and Time Formatter
Problem Statement
You are given six separate values representing date and time:
day
month
year
hour
minute
second

Your task is to format and print the date and time in the following exact format:
DD-MM-YYYY HH:MM:SS

Input Format
Six lines, each containing one value:
day
month
year
hour
minute
second

All values are strings and may contain leading zeros.

Output Format
Print a single line in the format:
DD-MM-YYYY HH:MM:SS

Example
Input
01
01
2021
12
30
00

Output
01-01-2021 12:30:00

Rules (IMPORTANT – Read Carefully)
You must not hardcode the output.

You must use:
string formatting
OR print() with sep and end
OR f-strings
OR .format()
OR % formatting

Do not use:
datetime library
any external library
Use only what you learned in Week 3."""

'''day = (input("Day:"))
month = (input("Month:"))
year = (input("Year:"))
hour = (input("Hour:"))
min = (input("Minutes:"))
sec = (input("Second:"))

print(f"{day}-{month}-{year}  {hour}:{min}:{sec}")
print("Second Method")
print(day,end ="-")
print(month,end="-")
print(year,end =" ")
print(hour,end =":")
print(min,end =":")
print(sec)
'''
# ===================================================================
# QUESTION — Financial Transaction Formatter
"""
Problem Statement
You are given three values related to a financial transaction:
country_code (string)
currency_code (string)
exchange_rate (float)

Your task is to print the transaction record in the following exact format:
<country_code>, <currency_code>, <exchange_rate_rounded_to_2_decimal_places>
The exchange rate must be rounded to exactly 2 decimal places.

Input Format
Three lines:
country_code
currency_code
exchange_rate

Output Format
Print a single line in this format:
IN, RS, 73.23
Example
Input
IN
RS
73.2272

Output
IN, RS, 73.23
Rules (IMPORTANT – Read Carefully)
You must round the float to exactly 2 decimal places
You must use formatted output:
f-string
OR .format()
OR % formatting

Do NOT:
use round() and then print directly
print the raw float
hardcode output
Use format specifiers."""

'''country_code = input("Country code:")
currency_code = input("Currency code:")
exchange_rate = float(input("Exchange rate:"))
print(f"{country_code},{currency_code}, {exchange_rate:.2f}")   # space after 2nd comma'''

#======================================================
# 🟦 QUESTION — Right Padding a String
"""
Problem Statement
You are given:
a single character string T
an integer n

Your task is to print the string T left-aligned in a field of width n, so that:
T appears at the start
and the remaining positions are filled with spaces on the right
In other words, you must add (n − 1) spaces after T.

Input Format
Two lines:
T
n
Where:
T is a single character string
n is a positive integer (n > 1)

Output Format
Print the padded string in this exact format:
T<spaces>
Total length of output must be exactly n characters.

Example
Input
A
5

Output
A    
(That is A followed by 4 spaces)
Rules (IMPORTANT)

You must use string formatting to achieve this:
% formatting
OR f-strings
OR .format()

Do NOT:
use loops to add spaces
use string multiplication (" " * k)
hardcode spaces

This problem is about format specifiers and alignment, not loops."""

'''T = input("Str:")
n = int(input("Enter int:"))
print(f"{T}{ "_"*(n-1)}")       # f-string method
print(T+(n-1)*"")               # normal print method
'''
# ======================================================================
# QUESTION — Caesar Cipher Encoder (Basic Version)
"""Problem Statement
You are given:
a lowercase string word
an integer shift

The English alphabet is:
abcdefghijklmnopqrstuvwxyz

Your task is to encode the word using a Caesar Cipher, where:
each letter is shifted forward by shift positions
if shifting goes beyond 'z', it must wrap around to the beginning

Input Format
Two lines:
word
shift

Where:
word contains only lowercase letters
shift is an integer between 0 and 25

Output Format
Print the encoded word.

Example
Input
5

Output
udymts

Rules (IMPORTANT)
You must:
loop through each character in the word
find its position in the alphabet
shift it forward by shift
use modulo (% 26) to wrap around

Do NOT:
use built-in encryption libraries
hardcode outputs
use ASCII shortcuts (for now)

Use only:
strings
loops
indexing
basic math"""

# Pseudocode
""" 
1) Define alphabet of English and result emplty string
2) Read the input word and shift variable 
3) Loop through the given word
    4) Find the position of current character in word
        # We do not care about position in the word.
        We only care about position in the alphabet.
    5) Find the postion of current char in Alphabet
    6) add the shift value to the current char position
    7) apply modulo operator on current char position to wrap
    8) add this to result 
9) print the result
"""
'''

alp = "abcdefghijklmnopqrstuvwxyz"
word = input("Enter word:")             # cons: it only accept lowercase, not uppercase
shift = int(input("Enter shift value:"))
result = ""                             # store encoded word
for char in word:
    position = alp.index(char)     # find position of character in alphabet 
    new_pos = (position + shift) % 26       # wrap logic and shifting the character
    new_char = alp[new_pos]         # give encoded character from alphabet 
    result += new_char

print(result)
'''

# ======================================================================
# 🟦 QUESTION — Sum of Single-Digit Numbers
"""
Problem Statement
You are given an integer n, followed by n integers.

Your task is to:
filter only the numbers that have exactly one digit
and compute their sum
Finally, print the sum.

Input Format
n
num1
num2
num3
...
numn

Where:
n is a positive integer
each num is an integer (can be positive or negative)

Output Format
Print a single integer — the sum of all single-digit numbers.

Example
Input
5
3
12
7
100
-4

Output
6

Explanation:
Single-digit numbers are: 3, 7, -4
Sum = 3 + 7 + (-4) = 6

Rules (IMPORTANT - Read Carefully)
A number is considered single-digit if:
its absolute value is less than 10
example: -4, 0, 7 are valid
example: 12, 100, -15 are NOT valid

You must:
read inputs using a loop
use filtering logic
use aggregation (sum)

Do NOT:
use built-in functions like sum() on a list
store all numbers in a list first (process one by one)
Process and add inside the loop."""
'''
n = int(input("enter the integer:"))
num_list = []                       # store list of entered number
sum_single = 0                      # store final result
# without storing the value in list is more professional becuase it save memory.
for i in range(n):
    x = int(input(f"Enter the number {i+1}: "))     # we can write f-string inside input too
    if abs(x) < 10:
        sum_single += x
print(sum_single)
'''

#===================================================
# 🟦 QUESTION — Double and Concatenate Strings
"""
Problem Statement
You are given an integer n, followed by n strings.

Your task is to:
double each string (repeat it twice)
add a single space after each doubled string
and concatenate everything into one final string
Finally, print the resulting string.

Input Format
n
s1
s2
s3
...
sn

Where:
n is a positive integer
each s is a string (may contain alphabets only, no spaces)

Output Format
Print a single line — the concatenated result.
Each doubled string must be followed by one space.

Example
Input

3
ab
x
cat

Output
abab xx catcat 

(Notice the space at the end — it is required)

Rules (IMPORTANT - Read Carefully)
You must:
read input using a loop
double each string using string operations
aggregate into one variable

Do NOT:
store all strings in a list and then join
use join()
print inside the loop

You must:
transform → then aggregate → then print once"""
'''
n_s = int(input("enter the integer:"))
concat_result = ""                  # store final result

for i in range(n_s):
    x_s = input(f"Enter string {i+1}:")
    doub_str = 2*x_s      
    # This add space after double string because intially conca-result is empty, so this avoid leading space      
    concat_result = concat_result +  doub_str + " "  
    # concat_result = concat_result  + " " +  doub_str  # this is correct but reverse the order
print(concat_result)
'''


# =========================================================
"""🟦 QUESTION — First Word Containing ‘a’
Problem Statement
You are given a sentence consisting of multiple words separated by spaces.

Your task is to:
scan the sentence word by word from left to right
find the first word that contains the letter 'a' (case-sensitive)
print that word
and stop processing further words immediately

Input Format
sentence

A single line containing the sentence.

Output Format
Print a single word — the first word that contains the letter 'a'.
If no word contains 'a', print nothing.

Example 1
Input
I love data science

Output
data

Example 2
Input
hello world python

Output
(no output, because no word contains 'a')
Rules (IMPORTANT – Read Carefully)

You must:
split the sentence into words
loop through words one by one
check for 'a' in each word
stop the loop as soon as you find the first match

You must use:
break to stop the loop

Do NOT:
collect all matching words
print multiple words
use list comprehensions

This is about search + early termination, not filtering all."""

def find_let_a_word(sentence:str) -> str:
    words = sentence.split()
    for w in words:
        if 'a' in w:
            print(w) 
            break
        


sent = "I love python data"
(find_let_a_word(sent))



#=====================================================
"""
Write code that:
takes input
splits it by space
prints index + word

Example input:
I love python

Output:
0 I
1 love
2 python

Rules:
must use split()
must use for
no enumerate (you are not ready yet)
manage index manually"""

def give_word_index(sentence):
    word = sentence.split()
    for i in range(len(word)):
         print(i,word[i])


sent = " I love python data "
give_word_index(sent)

#===========================================
# 🟦 QUESTION — Shift Characters Based on Vowel or Consonant
"""
Problem Statement
You are given a lowercase string sentence.

Your task is to:
process the string character by character

apply the following transformation:
    if the character is a vowel (a, e, i, o, u), replace it with the next character in the alphabet
    otherwise (consonant or any other character), replace it with the previous character in the alphabet
combine all transformed characters into a new string
print the final transformed string

Input Format
sentence
A single line containing a lowercase string.

Output Format
Print a single string — the transformed result.

Example
Input
cat

Output
bbs

Explanation
c → consonant → previous letter → b
a → vowel → next letter → b
t → consonant → previous letter → s
Final result: bbs
(Example output may vary depending on interpretation; follow the rules strictly.)

Rules (IMPORTANT – Read Carefully)
You must:
    loop through the string character by character
    check whether a character is a vowel
    use character shifting logic
    aggregate the result into a single string
    print once at the end

You must use:
    ord() to convert character → ASCII
    chr() to convert ASCII → character

Do NOT:
    use lists and join
    print inside the loop
    hardcode transformations
"""
s = "cat"
trans_char = ""         # store transformed word

for char in s:
    if char in "aeiou":     # don't write "a,e,i,o,u" as it also include ","
        # First ord() convert the char into number and add 1
        # after that chr() convert those number to character
        new_char = chr(ord(char) + 1)   # shift forward by character 1
    else:
        # we define char because we don't overwrite char, which is change the original value of char
        new_char = chr(ord(char) - 1)   # shift back by character 1

    trans_char += new_char          # add all transformed character
print(trans_char)

# ===========================================================
# 🟦 QUESTION — Nested Loop Accumulation
"""
Problem Statement
You are given a positive integer n.

Your task is to:
use nested loops
for each number i from 1 to n-1:
add the value of i to a running total exactly i times
after all loops finish, print the final total

Input Format
n

Where:
n is an integer greater than 1

Output Format
Print a single integer — the final accumulated total.

Example
Input
5

Output
30

Explanation (conceptual, not code)
When i = 1, add 1 → 1 time
When i = 2, add 2 → 2 times
When i = 3, add 3 → 3 times
When i = 4, add 4 → 4 times

The final total is the sum of all these additions.

Rules (IMPORTANT – Read Carefully)
You must:
use two loops (nested)
initialize an accumulator variable (e.g., total)
update the accumulator inside the inner loop

Do NOT:
use mathematical formulas
use lists
hardcode the output

This problem is about loop behavior, not shortcuts."""

n = int(input())
total = 0
for i in range(1,n):        # iterate from 1 to n-1
    for j in range(i):      # runs the loop i times
        total += i          # add the value of i exactly i times
    
print(total)