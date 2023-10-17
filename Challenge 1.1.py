def factorial(n):
    # Base case: factorial of 0 and 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: factorial of n is n times factorial of (n-1)
    else:
        return n * factorial(n - 1)
[0:50 pm, 06/09/2023] Hari ❤: result = factorial(int(input("Enter a number :")))  
print(result)