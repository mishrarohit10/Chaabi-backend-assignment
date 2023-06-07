#Calculate the factorial of a number using lambda function.?

# def factorial(n):
#     prod = 1
#     while n>0:
#         prod *= n
#         n -= 1
#     return prod


factorial = lambda x: 1 if x == 0 else x * factorial(x-1)

n = int(input("enter number -> "))
print(factorial(n))