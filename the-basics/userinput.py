#!/usr/bin/python3

def weather(temp):
    if temp > 60:
        print("Warm!!!")
    else:
        print("Cold!!!")


# input convert the enter value to string
user_in = input("Enter temperature: ")

# Need to convert the string to float before passing to weather function as it expects a number
weather(float(user_in))  