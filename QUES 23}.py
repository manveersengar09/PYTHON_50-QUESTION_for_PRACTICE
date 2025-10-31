# 23. Calculate Sum of a List of Numbers Using Recursion
# •	Write a recursive function to calculate the sum of a list of numbers.
# •	Example:
# Input: [1, 2, 3, 4, 5]
# Expected Output: 15
# •	Example:
# Input: [10, 20, 30]
# Expected Output: 60

def recursive_sum(numbers):
    # Base case: if list is empty, return 0
    if not numbers:
        return 0
    # Recursive case: first element + sum of the rest
    return numbers[0] + recursive_sum(numbers[1:])

# Ex:-1
print("Sum:", recursive_sum([1, 2, 3, 4, 5]))   # Expected Output: 15

# Ex:-2
print("Sum:", recursive_sum([10, 20, 30]))      # Expected Output: 60
