# for loop on a list
my_list = [5, 3, 6, 8, 4, 0.5, 2.6]

for item in my_list:
    if item % 2 == 0:
        print(item)
    else:
        print(f"{item} is odd")
