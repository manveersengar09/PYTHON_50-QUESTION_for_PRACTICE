# QUES} 17. Convert Decimal to Binary
# •	Write a function to convert a given decimal number to its binary representation.
# •	Example
# Input: decimal = 10
# Expected Output: 1010 (the binary representation of 10 is 1010)
# •	Example
# Input: decimal = 5
# Expected Output: 101 (the binary representation of 5 is 101)


def decimal_to_binary(n):
    # Base case
    if n == 0:
        return ''
    else:
        # Recursive call: divide number by 2 and store remainder
        return decimal_to_binary(n // 2) + str(n % 2)

# Ex:-1
decimal = 10
binary = decimal_to_binary(decimal)
print("Binary representation of", decimal, "is:", binary)

# Ex:-2
decimal = 5
binary = decimal_to_binary(decimal)
print("Binary representation of", decimal, "is:", binary)
