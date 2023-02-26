# ////////// pattern printing

# problem 2

# need ASCII to write alphabets
# chr print alphabet ( 65 = A , 97 = a )

for row in range(0,10):
    for col in range( row + 1 ):
        print(chr(97+row), end = " ")
    print()