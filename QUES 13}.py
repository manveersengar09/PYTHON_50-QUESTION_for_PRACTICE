# QUES 13}
""" 
Generate List of Even Numbers
•	Create a function that generates a list of even numbers up to a given number.
•	Example
Input: n = 10
Expected Output: [2, 4, 6, 8, 10]
•	Example
Input: n = 7
Expected Output: [2, 4, 6]

"""

def even(n):
    even_num = []
    for i in range(2,n+1,2):
        even_num.append(i)
    return even_num 
#INPUT
n = int(input("enter a number :- ".upper()))
print(f"even number up to {n} : {even(n)}".upper())