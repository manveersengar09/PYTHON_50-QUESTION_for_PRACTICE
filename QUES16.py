# 16. Calculate GCD Using Euclidean Algorithm
# •	Write a function to find the Greatest Common Divisor (GCD) of two numbers using recursion.
# •	Example
# Input: a = 48, b = 18
# Expected Output: 6 (the GCD of 48 and 18 is 6)
# •	Example
# Input: a = 56, b = 98
# Expected Output: 14 (the GCD of 56 and 98 is 14)

def gcd(a, b):
    # Base case: if b becomes 0, a is the GCD
    if b == 0:
        return a
    else:
        # Recursive case: gcd(b, a % b)
        return gcd(b, a % b)

# Ex:- 1
a, b = 48, 18
print("GCD of", a, "and", b, "is:", gcd(a, b))

# Ex:- 2
a, b = 56, 98
print("GCD of", a, "and", b, "is:", gcd(a, b))
