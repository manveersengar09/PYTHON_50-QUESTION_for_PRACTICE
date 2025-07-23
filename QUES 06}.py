# QUES 6}
#  Check for Anagram
# •	Write a program to check if two input strings are anagrams of each other.
# •	An anagram is a word or phrase that is formed by rearranging the letters of another word or phrase. To be anagrams, two strings must contain the exact same characters in the same quantities, but in any order.
# •	Example: "listen" and "silent" are anagrams.

str1 = input("ENTER A WORD :- ").lower()
str2 = input("ENTER A WORD :- ").lower()
#CHECK FIRST LEN OF BOTH IS SAME OR NOT
if len(str1) == len(str2):
# THEN SORTED IT 
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
#CHECK SORTED IS SAME IN BOTH 
    if sorted_str1 == sorted_str2:
        print(f"THIS {str1} AND {str2} are anagram ")
    else:
        print("THIS IS NOT AN ANAGRAM ")
else:
    print("THIS IS NOT AN ANAGRAM")