# QUES 2}
# Reverse the string using for loop.
# string = "Python"
# Expected output = "nohtyP"

string =str(input("ENTER A WORD :- ")) 
rev = " "
for item in string:
    rev = item + rev

print(f"the reverse is {rev}")
