# QUES 4}
 
# Calculate factorial of a number
# Example: If number is 5 factorials will be (5x4x2x3x2x1=120)
# Expected output: 120 if number is 5

user = int(input("ENTER A NUMBER :- "))
total = 1
for i in range(user,1,-1):
    total *= i
print (f"THE FACTORIAL OF A NUMBER {user} IS {total}")

                          # OR BY USING def
''' 
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # Output: 120
 
 '''