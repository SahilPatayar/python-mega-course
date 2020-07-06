#!/usr/bin/python3

name = input("Enter first name: ")
last_name = input("Enter Last name: ")

# String format way 1
message1 = "Hello %s %s!" %(name, last_name)
message2 = "Hello {} {}!".format(name, last_name)

print(message1)
print(message2)