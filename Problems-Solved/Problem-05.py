# Write a Program to check weather a year is leap year or not.Take input from user.

year = int(input("Enter a Year to see is it leap year or not : "))

if year%400 == 0 and year%100 == 0:
    print("This is a Leap year.")
elif year%4 == 0 and year%100 != 0:
    print("This is an Leap year.")
else :
     print("This is not a Leap year.")