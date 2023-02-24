# For loop
# ///////////////
a = "Hello World"

for letter in a :
    print(letter)

# ///////////////
# Test - 02

Box = [ "Egg" , "Sugar" , "Ice Cream"]

for list in Box:
    print(list)

# //////////////
# Test - 03

horses_number = [ 3, 6 ,9 ,10 ,11 ,12 ,13 , 6 ]
for number in horses_number:
    if number <= 10:
        print(number)


# /////////////////
# Test - 04
# 3 and 5 divideble numbers.

for i in range(30):
    if (i % 3 == 0) and (i % 5 == 0):
        print(i)


# //////////////////
# Test - 05
# 1+2+3

number = 0
for i in range(1,20):
    number = number + i
print(number)
