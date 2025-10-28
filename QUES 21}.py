# QUES:-21. Find Intersection of Two Lists
# •	Write a function that returns the intersection of two lists without using set operations.
# •	Example:
# Input: list1 = [1, 2, 3, 4, 5], list2 = [4, 5, 6, 7, 8]
# Expected Output: [4, 5]
# •	Example:
# Input: list1 = ['apple', 'banana', 'cherry'], list2 = ['cherry', 'date', 'apple']
# Expected Output: ['apple', 'cherry']


# Func to find intersection of two lists without using set
def find_intersection(list1, list2):
    intersection = []
    for item in list1:
        if item in list2 and item not in intersection:
            intersection.append(item)
    return intersection

# Ex:- 1
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print("Intersection:", find_intersection(list1, list2))

# Ex:- 2
list1 = ['apple', 'banana', 'cherry']
list2 = ['cherry', 'date', 'apple']
print("Intersection:", find_intersection(list1, list2))
