# QUES 08}
# . Sum of Digits
# •	Write a function that takes an integer as input and returns the sum of its digits.
# •	Example: sum_of_digits(123) -> 6


def sum(number):
    total = 0
    for digit in str(abs(number)):  
        # Convert number to string and handling negative input 
        total += int(digit)
    return total

# Example usage:
num = int(input("Enter a number: "))
print(f"Sum of digits of {num} is {sum(num)} ")
