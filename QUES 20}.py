# QUES :-20. Count Occurrences of Each Character in a String
# •	Take a string as input and count the occurrences of each character.
# •	Example:
# Input: "hello"
# Expected Output: { 'h': 1, 'e': 1, 'l': 2, 'o': 1 }
# •	Example:
# Input: "apple"
# Expected Output: { 'a': 1, 'p': 2, 'l': 1, 'e': 1 }




def count_characters(text):
    char_count = {}  
# Empty dictionary to store counts
    
    for char in text:
        if char in char_count:
            char_count[char] += 1  
        # Increase count if character already exists
        else:
            char_count[char] = 1   # Add new character with count 1
            
    return char_count


# Ex:- 1
print(count_characters("hello"))  
# OuT: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Ex:- 2
print(count_characters("apple"))  
# Out: {'a': 1, 'p': 2, 'l': 1, 'e': 1}
