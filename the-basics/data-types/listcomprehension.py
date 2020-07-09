#! /usr/bin/python3

list_of_numbers = [ 1, 2, 3, 4, 5]

print(list_of_numbers)

even_the_list = [i * 2 for i in list_of_numbers]

print(even_the_list)

# list comprehension with if condition

even_list_3_above = [i * 2 for i in list_of_numbers if i > 3]

print(even_list_3_above)

# list comprehension with if else condition
another_list = [i * 2 if i > 3 else 9 for i in list_of_numbers]

print(another_list)

