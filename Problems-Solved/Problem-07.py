# program to find the factorial of a given Number.

a = int(input(" Enter a valid number = "))

factorial = 1

for i in range(1,a+1):
    factorial = factorial*i
print(factorial)