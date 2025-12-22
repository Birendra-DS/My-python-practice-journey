''' You are helping IITM’s “Student Information Processing System” build a small tool that processes student data.
Given several pieces of input (integers, floats, strings, dates), write Python code to compute the required values.

All input will be provided in the order described.
You must assign each answer to the correct variable as shown.'''

#===================================================

'''🟦 PART 1 — Arithmetic operations

Given two integers a and b, compute:
output1 = sum of a and b
output2 = twice the sum of a and b
output3 = absolute difference between a and b
output4 = absolute difference between (a + b) and (a * b)'''

# ===========================================================
def arithmetic_ops(a,b):
    output1 = a + b
    output2 = 2*output1
    output3 = abs(a-b)
    output4 = abs(output1 - (a*b))            # Also-> abs((a+b) - (a*b))
    return output1, output2, output3, output4
# ===========================================================

'''🟩 PART 2 — Discounts & rounding

Given:
price (int)
discount_percent (float)

Compute:
discounted_price = price – (price * discount_percent / 100)
rounded_discounted_price = discounted_price rounded to nearest int
'''

# ===========================================================
def marketing(price, discounted_percent):
    # compute how much discount is given
    discount_amount = price * (discounted_percent / 100)       # just to make code more readable
    discounted_price = price - discount_amount      #Direct method: discounted_price = price - (price * (discounted_percent/100)) 
    rounded_discounted_price = round(discounted_price)
    return discounted_price, rounded_discounted_price
# ===========================================================

'''🟧 PART 3 — Time conversion

Given:
total_mins (int)

Compute:
hrs = number of hours (floor division)
mins = remaining minutes'''

# ===========================================================
def time_convert(total_mins):
    hrs = total_mins // 60      # use // for hours calculation from mins 
    mins = total_mins % 60      
    return hrs, mins
# ===========================================================

'''🟨 PART 4 — Boolean conditions on integers
Given integer a, compute:
output1 = True if a >= 5
output2 = True if a is divisible by 5
output3 = True if a is odd and < 10
output4 = True if a is odd and between -10 and 10
output5 = True if a has even number of digits but not more than 10 digits'''

# ===========================================================
def bool_cond(a):
    output1 = True if a>=5 else False   # I can also use a>=5 directly without if and else as it give the same result. Because it automatically do that work
    output2 = True if a%5 == 0 else False       # Also a%5 == 0, but I have doubt that how it return True and false⁉️
    output3 = True if a % 2 != 0 and a<10 else False     # ⁉️can it a%2 !=0 and a<10
    output4 = True if (a % 2 != 0) and (-10 < a < 10) else False    # Use parenthesis in both side. Also-->(a % 2 != 0) and (-10 < a < 10)

    #output5 = True if len(a) % 2 == 0 and len(a) <=10 else False-> this is wrong becuase we need len(str(abs(a))) to get absolute value length
    digit = len(str(abs(a)))        # len(str(abs(a))) correctly handles negative numbers and avoids runtime errors when counting digits.
    output5 = digit % 2 == 0 and (digit<=10)
    return output1, output2, output3,output4, output5

# ===========================================================
'''🟪 PART 5 — String slicing

Given a string s, compute:
output1 = third character of s
output2 = fourth last character of s
output3 = first three characters of s
output4 = every second character of s
output5 = last three characters of s
output6 = reverse of s'''

# ===========================================================
def char(s):
    output1 = s[2]
    output2 = s[-4]
    output3 = s[:3]
    output4 = s[::2]
    output5 = s[-3:]    # I get trouble in this
    output6 = s[::-1]
    return output1,output2,output3,output4,output5,output6

#s = 'Birendra'
#print(char(s))
# ===========================================================

'''🟫 PART 6 — Course code parsing
Given course code string formatted as "DS1023", where:
first two letters = department
next two = term(two-digit)
last two = year(two-digit)

Compute:
course_term = the term as integer
course_year = the year as integer'''
# ===========================================================
def course_code(s):
    #return the course_term as integer
    course_term = int(s[2:4])
    #return the course_year as integer
    course_year = int(s[-2:-1])
    return course_term, course_year

s = "DS1023"
print(course_code(s))
# ===========================================================
'''🟦 PART 7 — Word operations

Given:
word1, word2, word3 (strings)
n1, n2 (integers)
Compute:
output1 = word1 + " " + word2
output2 = first 4 letters of word1 + "-" + last 4 letters of word2
output3 = word3 + " " + str(n1)
output4 = "-" repeated 50 times
output5 = "-" repeated n2 times
output6 = string of n1 repeated n2 times
Booleans:
are_all_words_equal = True if all 3 words are equal
is_word1_comes_before_other_two = True if word1 < word2 < word3  (alphabetically)
has_h = True if word1 contains letter "h" (case-insensitive)
ends_with_a = True if word1 ends with "a" or "A"
has_the_word_python = True if the sentence contains "python"'''

# ===========================================================
def data(word1, word2, word3, n1,n2):
    output1 = word1+" "+ word2
    output2= word1[0:4] + "-" + word2[-4:]      # don't write word2[-4:-1]
    output3 = word3 + " " + str(n1)
    output4 = "-" * 50
    output5 = "-" * n2
    output6 = str(n1) * n2
    return output1, output2, output3, output4, output5, output6

word1 = "Birendra"
word2 = "AjayBalmiki"
word3 = "Elon"
n = 5
n2 = 2

print(data(word1, word2, word3, n,n2))

'''🟥 PART 8 — Date parsing (dob) & birthdays

Input:
age (int)
dob formatted as "dd/mm/yy"
Extract:
day, month, year = integers from dob
Compute:
fifth_birthday = dob but year + 5  (print as dd/mm/yyyy)
last_birthday = dob but year + age (dd/mm/yyyy)
tenth_month = dob advanced by 10 months (dd/mm/yyyy)
No need to worry about zero-padding, write natural formatting.'''
# ===========================================================
def Birth_data(age, dob):
    year = dob[-2:]
    fifth_birthday = int(year) + 5
    last_birthday = year + "age"
    return f"{fifth_birthday}, \n{last_birthday}"

age = 20
dob = "04/06/05"
print(Birth_data(age, dob))
# ===========================================================
'''🟩 PART 9 — Weight formatting
Given:
weight (float)

Format as:
weight_readable = "XX kg YY grams"

Where:
integer part = kg
decimal part × 1000 = grams (rounded to nearest int)'''

def weight_read(weight):
    kg_wgt = int(weight)
    decimal_wgt = weight - kg_wgt
    gram_wgt = f"{decimal_wgt * 1000:.2f}"          # it is use to round of the gram value up to 2 decimal point
    weight_readable = f"{kg_wgt} kg {gram_wgt} grams"
    return (weight_readable)

weight_readable = 52.247 
print(weight_read(weight_readable))

# ===========================================================

'''🟦 FINAL OUTPUT REQUIREMENTS

Print output in this exact order, each on a new line:

All arithmetic results

discounted_price, rounded_discounted_price

hrs, mins

boolean results

string slicing outputs

course_term, course_year

all word outputs

all boolean word outputs

tenth_month, fifth_birthday, last_birthday

weight_readable'''
# ===========================================================