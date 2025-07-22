# QUES 03} 
# . Palindrome Check (String Problem)
# Write a function to check whether a given string is a palindrome (a string that reads the same
# forward and backward is called palindrome).
# String = “mom” # if we reverse this string, we get the same Output “mom”
# Expected output: string is a palindrome.


string =str(input("ENTER A WORD :- ")) 
reversed_string = string[::-1]
if reversed_string == string:
    print(f"{string} is a palindrome ")
else:
    print(f"{string} is not a palindrome")

    