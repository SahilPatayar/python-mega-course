#! /usr/bin/python3

# list hold collection

daily_temps = [72.5, 79.8, 80.5]

temp_sum = sum(daily_temps)
print("Sum of everyday temperature: ", temp_sum)

length = len(daily_temps)
print("Length: ", length)

average_temp = temp_sum / length

print(average_temp)

# tuple example
tuple_of_vowels = ('a', 'e', 'i', 'o', 'u')

# 1. Find maximun
print("Max temp: ", max(daily_temps))

# 2. Find count of 72.5
print("Count of 72.5", daily_temps.count(72.5))
print("Count of 72.0", daily_temps.count(72.0))

###
# More on lists
###

simple_list = [9, 10, 5, 4, 6]

# append
simple_list.append(15)

# find 0 based index
simple_list.index(10)

# insert item at provided index
simple_list.insert(1, 22)

first_item = simple_list[0]



###
# Slicing list
###

# print items from index 0 to 2
print(simple_list[0:2])
print(simple_list[:2])

# print last two items - 
print(simple_list[-2:])


