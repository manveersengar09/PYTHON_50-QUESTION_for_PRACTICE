# QUES 10}
# Remove Duplicates from a List
# •	Write a function that removes duplicates from a list while maintaining the original order.
# •	Example
# Input: [1, 3, 2, 3, 4, 1, 5]
# Expected Output: [1, 3, 2, 4, 5]
# •	Example
# Input: [4, 4, 4, 4]
# Expected Output: [4]

def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

# Example usage:
print("INPUT :- ",remove_duplicates([1, 3, 2, 3, 4, 1, 5]))  
print("OUTPUT :- ",remove_duplicates([4, 4, 4, 4]))           