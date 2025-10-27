# 19. Find Largest Element in a List Using for Loop
# •	Write a function to find the largest element in a list without using built-in max functions.
# •	Example
# Input: [3, 5, 7, 2, 8, 1]
# Expected Output: 8 (the largest element in the list is 8)
# •	Example
# Input: [-1, -5, -3, -4]
# Expected Output: -1 (the largest element in the list is -1)

                                                                                                                                                
def find_largest(numbers):
 # Assume the 1st element is the largest initially
    largest = numbers[0]
# Loop through each number in the list
    for num in numbers:
        if num > largest:
            largest = num  # Update if current number is larger
    
    return largest

# Ex:- 1
print(find_largest([3, 5, 7, 2, 8, 1]))  # Output: 8

# Ex:- 2
print(find_largest([-1, -5, -3, -4]))    # Output: -1
