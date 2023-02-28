# Take three integer input from user and find the largest number between using if-elif-else statement.

first_number = int(input("Enter a First number : "))
second_number = int(input("Enter a Second number : "))
third_number = int(input("Enter a Third number : "))

if first_number > second_number and first_number > third_number:
    print("This is the largest number :", first_number,".")
elif second_number > first_number and second_number > third_number:
    print("This is the largest number :", second_number,".")
else:
    print("This is the largest number :", third_number,".")
