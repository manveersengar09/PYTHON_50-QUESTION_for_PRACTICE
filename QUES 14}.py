# # QUES 14} Binary Search Implementation
# •	Write a function that performs binary search on a sorted list and returns the index of the target element or -1 if not found.
# •	Example
# Input: sorted_list = [1, 2, 3, 4, 5, 6], target = 4
# Expected Output: 3 (since 4 is at index 3)
# •	Example
# Input: sorted_list = [10, 20, 30, 40, 50], target = 25
# Expected Output: -1 (since 25 is not in the list)

# QUES 14: Binary Search Implementation

def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    
    while low <= high:
        mid = (low + high) // 2   # Find middle index
        if sorted_list[mid] == target:
            return mid   # Found target
        elif sorted_list[mid] < target:
            low = mid + 1   # Search in right half
        else:
            high = mid - 1  # Search in left half
    return -1   # Not found

# Example 1
sorted_list = [1, 2, 3, 4, 5, 6]
target = 4
print("Index of", target, ":-", binary_search(sorted_list, target))  
# Output → 3

# Example 2
sorted_list = [10, 20, 30, 40, 50]
target = 25
print("Index of", target, ":-", binary_search(sorted_list, target))  
# Output → -1 
