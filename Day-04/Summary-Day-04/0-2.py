# //////////// range function with list


# can't use range in while loop


# without for loop:

list = list(range(10))
print(list) # [ 0,1,2,3,4,5,6,7,8,9]

# with for loop:

for list in range (10):
    print(list) # [ 0,1,2,3,4,5,6,7,8,9]

# ////////////// parameters in range function ( start , end , step)

r1 = list(range(5))
r2 = list(range(2,5))
r3 = list(range(1,10,3))
r4 = list(range(-5,10,3))

print(r1) # [ 0,1,2,3,4 ]
print(r2) # [ 2,3,4 ]
print(r3) # [ 1,4,7 ]
print(r4) # [ -5,-2,1,4,7 ]