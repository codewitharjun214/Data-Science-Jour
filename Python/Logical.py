"""
Python Logical Operators
------------------------

Logical operators are used to combine conditional statements.
They are mainly used with comparison operators.

Logical Operators in Python
---------------------------
and   Returns True if both conditions are True
or    Returns True if at least one condition is True
not   Reverses the result (True → False, False → True)
"""

# =========================
# 1. Logical AND (and)
# =========================
# Both conditions must be True
print("(5 > 3) and (2 < 4) =", (5 > 3) and (2 < 4))   # True
print("(5 > 3) and (2 > 4) =", (5 > 3) and (2 > 4))   # False


# =========================
# 2. Logical OR (or)
# =========================
# At least one condition must be True
print("(5 > 3) or (2 > 4) =", (5 > 3) or (2 > 4))     # True
print("(5 < 3) or (2 > 4) =", (5 < 3) or (2 > 4))     # False


# =========================
# 3. Logical NOT (not)
# =========================
# Reverses the result
print("not (5 > 3) =", not (5 > 3))                   # False
print("not (5 < 3) =", not (5 < 3))                   # True


"""
Important Notes:
----------------
1. 'and' requires all conditions to be True.
2. 'or' requires at least one condition to be True.
3. 'not' reverses the Boolean result.
4. Logical operators are commonly used in if-else statements.
"""
