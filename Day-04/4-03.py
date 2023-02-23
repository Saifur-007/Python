successful = True
for number in range(10):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 10 time and failed")