# /////////////// traversing nested list

box = [["Egg","Onion"], ["Pizza",2.5,3], [12,13,15]]

for item in box:
    for each_item in item:
        print(each_item)
#       /// display every item.