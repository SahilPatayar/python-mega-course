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