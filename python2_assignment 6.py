'''
Implement a recursive function to compute the nth Fibonacci number.
Instructions:
Write a recursive function fibonacci(n) that returns the nth Fibonacci number.
The Fibonacci sequence is defined as:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1
Write test cases to verify the function works correctly for different values of      n.
'''

def fibonacci(n):

    if n==0:
        return 0
    if n==1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci is, ", fibonacci(7))