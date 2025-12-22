# ===============================================================
# Q1. Which of the following are valid variable names in Python?
# a_, _a, 1a, a variable, a_variable
    # My thinking:
        # - Python variables cannot start with a number
        # - They cannot contain spaces
        # - They can start with underscore
a_ = 2
_a = 2

print(_a)
print(a_)

# Uncommenting below lines will cause errors:
    # 1a = 5
    # a variable = 6
# ========================================================

# =========================================================
# Q2: 
word_1 = "Hello"
word_2 = "Elon"
print(word_1 + word_2)
#print(word_2 + word_1)

temp = word_1
word_1 = word_2
word_2 = temp
print(word_1 + word_2)  # Now word_1 = Elon nad word_2 = Hello

# Observstion:
    #1. Both print statement are only same when both word_1 == word_2
    # we can use a third variable to swap the value of the variable easily

# Same code using function
def swap(word_1, word_2):
    L1 = word_1 + word_2
    # using the three assignment
    word = word_1
    word_1 = word_2
    word_2 = word
    L2 = word_1 + word_2
    return L1, L2
# ======================================================

# ======================================================
