# QUES NO:- 7
# Count Vowels in a String
# •	Take a string as input and count the number of vowels (a, e, i, o, u) in it.
# •	Example: “Python” word has 1 vowel sound(o)


str = input("ENTER A WORD :- ").lower()
count = 0

for i in str:
    if i in ("a", "e", "i", "o", "u"):
        count += 1

print(f"THE WORD '{str}' CONTAINS {count} VOWELS.")
