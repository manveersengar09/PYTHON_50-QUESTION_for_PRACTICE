# 22. Remove All Whitespace from a String
# •	Write a function that removes all whitespace characters (spaces, tabs, newlines) from a given string.
# •	Example:
# Input: "Hello, World!"
# Expected Output: "Hello,World!"
# •	Example:
# Input: " Python is fun "
# Expected Output: "Pythonisfun"

#Remove All Whitespace from a String
#Write a function that removes all whitespace characters (spaces, tabs, newlines) from a given string.

def remove_whitespace(text):
# Removes all types of whitespace (spaces, tabs, newlines)
    return "".join(text.split())

# Example 1
text1 = "Hello, World!"
print(remove_whitespace(text1))   # Expected Output: Hello,World!

# Example 2
text2 = " Python is fun "
print(remove_whitespace(text2))   # Expected Output: Pythonisfun
