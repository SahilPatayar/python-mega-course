#!/usr/bin/python3

temp_list = [64, 72, 98]

temp_dict = {"Mon": 64, "Tue": 72, "Wed": 98}

# for loop
for temp in temp_list:
    print(temp)

for pair in temp_dict.items():
    print(pair)

for key, value in temp_dict.items():
    print(key + ":", value)


# while loop

user_in = ""

while user_in != 'sahil':
    user_in = input("Please Enter username: ")

# Another above code variation

while True:
    user_in = input("Please Enter username: ")
    if user_in == "sahil":
        break
    else:
        continue


