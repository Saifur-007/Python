print("Select an operation to perfrom: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

#code for add
if operation == "1" :
    num1 = input("Enter first number: ")
    num2 = input("Enter second number:")
    print("The result is " + str(int(num1) + int(num2)))
#code for subtract
elif operation == "2" :
    num1 = input("Enter first number: ")
    num2 = input("Enter second number:")
    print("The result is " + str(int(num1) - int(num2)))
#code for multiply
elif operation == "3" :
    num1 = input("Enter first number: ")
    num2 = input("Enter second number:")
    print("The result is " + str(int(num1) * int(num2)))
#code for division
elif operation == "4" :
    num1 = input("Enter first number: ")
    num2 = input("Enter second number:")
    print("The result is " + str(int(num1) / int(num2)))
else:
    print("Invalid Entry")
    