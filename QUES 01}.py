# 1. Take the input from user and find whether number is prime or not?
#    " Prime numbers are number which are divide by 1 or themselves only. "
# Example: 13 is a prime number.
# Example: 97 is a prime number 
user = int(input("ENTER A NUMBER "))
if user <= 1:
    print(f"{user} is not a prime number")
else:
    for i in range(2, user):
        if user % i == 0:
            print(f"{user} is not a prime number")
            break
    else:
        print(f"{user} is a prime number")
