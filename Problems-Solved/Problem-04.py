#Write a Program to take integer input from user and display the grade according to the Criteria.

# > 90 -- A
# > 80 and <= 90 -- B
# >= 60 and <= 80 -- C
# below 60 -- D

mark = int(input("Enter your mark to see ,What you Got : "))

if mark > 90 and mark <= 100:
    print( "Congratulations you got = A .")
elif mark > 80 and mark <= 90:
    print("Congratulations you got = B .")
elif mark >= 60 and mark <= 80:
    print("Congratulations you got = C .")
elif mark <60:
    print("Congratulations you got = D .")
else :
    print("Enter a Valid mark.")