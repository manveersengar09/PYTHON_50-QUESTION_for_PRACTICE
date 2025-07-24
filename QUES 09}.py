#  QUES 09}
#  Fibonacci Sequence (Iterative)
# •	Write a function that prints the first n numbers in the Fibonacci sequence.
# •	Use an iterative approach.
# •	Example
#  Input: n = 6
#  Expected Output: 0, 1, 1, 2, 3, 5
# •	Example
#  Input: n = 1
#  Expected Output: 0

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=", " if i < n - 1 else "") 
        a, b = b, a + b

# Example usage:
num = int(input("Enter how many Fibonacci numbers you want: "))
fibonacci(num)
