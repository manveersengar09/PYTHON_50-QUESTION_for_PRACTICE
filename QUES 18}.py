
# QUES} 18. Factorial Using Recursion
# •	Write a recursive function to calculate the factorial of a given number.
# •	Example
# Input: n = 5
# Expected Output: 120 (since 5×4×3×2×1=120)
# •	Example
# Input: n = 0
# Expected Output: 1 


def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)

# Ex:-1
n = 5
print("Factorial of", n, "is:", factorial(n))

# Ex:- 2
n = 0
print("Factorial of", n, "is:", factorial(n))
