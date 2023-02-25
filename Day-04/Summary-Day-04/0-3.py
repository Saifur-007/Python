# /////// more about for loop

# letter:

m1 = "Hello World"
for letter in m1:
    print(letter) # display every letter


# item:

m2 = [ "Egg" , "Cake" , 3,4,6,0 ]
for item in m2:
    print(item) # display every item

# filter:

m3 = [ 12,45,30,44 ]
for i in m3:
    if i<= 44:
        print(i) # 12 , 30 , 44


# divisible number :
for i in range(50):
    if (i % 3 == 0) and (i % 5 == 0) :
        print(i) # 0,15,30,45

# sum :

sum = 0
for i in range (1,11):
    sum = sum + i # update variable
print(sum)