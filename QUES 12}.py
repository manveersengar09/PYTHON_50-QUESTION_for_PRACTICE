# QUES 12} 
"""
Calculate Power without Using ** Operator
•	Write a function that calculates xy  (x raised to the power of y) without using Python’s power operator (**).
•	Example
Input: x = 2, y = 3
Expected Output: 8 (since 23 =8)

"""
def power (x,y):

    result = 1

    for _ in range(abs(y)):
    # use of "_" is default value '-'
        result *= x 
    if y < 0:
        return 1 / result
    return result


# Example usage:
print(power(2, 3))   # Output: 8   (since 2^3 = 8)
print(power(5, 0))   # Output: 1   (since any number to the power 0 is 1)
print(power(2, -2))  # Output: 0.25  (since 2^-2 = 1/4 = 0.25)