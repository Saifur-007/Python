# ///////// break vs continue

# with for loop:

for i in range(10):
    if i == 5:
        break
    print(i) # 0,1,2,3,4

for i in range (10):
    if i == 5:
        continue
    print(i) # 0,1,2,3,4,6,7,8,9

# with while loop:

a = 0
while a <= 10:
    a = a+1
    if a == 5:
        break
    print(a) # 1,2,3,4

a = 0
while a <= 10:
    a = a+1
    if a == 5:
        continue
    print(a) # 1,2,3,4,6,7,8,9,10,11
    # 11 = increment before printing
