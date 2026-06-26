"""
Python Assignment Operators
---------------------------

Assignment operators are used to assign values to variables.
They can also perform an operation and assign the result in one step.

Basic Assignment
----------------
=   Assigns a value to a variable

Compound Assignment Operators
-----------------------------
+=  Add and assign
-=  Subtract and assign
*=  Multiply and assign
/=  Divide and assign
"""

# =========================
# 1. Basic Assignment (=)
# =========================
x = 5
print("Initial value of x:", x)   # Output: 5


# =========================
# 2. Add & Assign (+=)
# =========================
# x += 3  means  x = x + 3
x += 3
print("After x += 3:", x)         # Output: 8


# =========================
# 3. Subtract & Assign (-=)
# =========================
# x -= 3  means  x = x - 3
x -= 3
print("After x -= 3:", x)         # Output: 5


# =========================
# 4. Multiply & Assign (*=)
# =========================
# x *= 3  means  x = x * 3
x *= 3
print("After x *= 3:", x)         # Output: 15


# =========================
# 5. Divide & Assign (/=)
# =========================
# x /= 3  means  x = x / 3
x /= 3
print("After x /= 3:", x)         # Output: 5.0


"""
Important Notes:
----------------
1. /= always returns a float value in Python.
2. Compound assignment operators make code shorter and cleaner.
3. These operators are commonly used in loops and calculations.
"""
