# Parameter writing technique
Think of two separate jobs:
Getting data (user input, files, APIs).
Doing work with that data (calculations, printing tables, etc.).

Professional Python code tries hard to separate these two.​

## Why not put input() in the parameter?
    Your version:
    python
    def mult_table(n = int(input("Enter a no: "))):
        ...

    Problems:
    Evaluated once at definition time
    Default parameter values are calculated only once, when Python first reads the def.

    That means input() is called once, and the answer is “frozen” into the default n.
    If you later call mult_table() many times, it will silently reuse that same n without asking again. That’s surprising behavior.
    Harder to test and reuse
    You cannot easily call mult_table(5) from another script or a unit test without the input prompt happening at import time.
    Good functions should work like math functions: same input → same output, no hidden I/O.

## Mixes concerns
    A function should ideally “do one thing well”. Here it’s doing both: reading input and printing the table.
    Keeping I/O at the top level and logic inside functions makes programs easier to understand and change.

## Why read input at the call site?
    Recommended structure:
    python
    def mult_table(n):
        for i in range(1, 11):
            print(n * i)

    n = int(input("Enter a no: "))
    mult_table(n)
    Benefits:
    mult_table is a pure “logic” function: given an n, it prints the table.
    input() is only called where you see it clearly.
    ​
    In the future, you can reuse mult_table(7) with data from a file, or another function, without changing its code.

    A mental rule that helps:
    “Functions should receive data, not fetch it themselves, unless their whole job is I/O.”


# Factor finding 
## print vs return
    print() just shows data to the user and then it’s gone.

    return sends data back to the caller so it can be stored, reused, tested, etc.

    A function with only prints is hard to reuse in real projects; a function that returns data is reusable and testable.

    Use:
    python
    def get_factors(n: int) -> list[int]:
        """Return all factors of n in increasing order."""
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors

    n = int(input())
    print(get_factors(n))
    Key rule:

    Printing is for humans; returning is for programs.
    Most functions in professional code return data, and the outermost code decides when to print.

## Why return needs a list
    return stops the function immediately.

    If you write:

    python
    def get_factors(n: int) -> list[int]:
        for i in range(1, n + 1):
            if n % i == 0:
                return i
    it will return only the first factor (usually 1) and exit.

    To return all factors, you must:
    Create a list: factors = [].
    append(i) each time i is a factor.
    return factors once at the end.

## Type hints: parameters and return types
    These are only for clarity and tooling; Python doesn’t enforce them at runtime.

    def get_factors(n: int) -> None:
    n: int means “n should be an integer”.

    -> None means “this function doesn’t return a useful value” (it probably prints).

    def get_factors(n: int):
    Same runtime behavior; just no return type hint.
    Valid return type hints for lists:

    -> list[int] ✅ best: “returns a list of ints”
    -> list ✅ valid: “returns some list, element type unspecified”
    -> list(int) ❌ invalid syntax
    -> list{int} ❌ invalid syntax

    The arrow must be exactly ->, with nothing extra (no ------->, no >>>>).

4. Clean function design (professional mindset)
    One function = one responsibility.
    Good pattern:
    Function: compute and return data, no prints.
    Caller: decides whether to print or log the result.
    Printing inside utility functions makes them harder to reuse, test, and compose into pipelines.
