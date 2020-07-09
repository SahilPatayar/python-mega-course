#!/usr/bin/python3

r'''
Problem:

Make a program which 
1. Accepts input from user
2. Capitalize first letter of input
3. if sentense is question, then append question mark in the end else a period.
4. exit program when user type '\end' and print everything nicley

'''


inputs = []

def sentense_maker(phrase):
    capitalized = phrase.capitalize()

    if capitalized.startswith(("How","What","Why", "Where")):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

while True:
    user_in = input("Say Something! ")
    if user_in == r'\end':
        print(" ".join(inputs))
        break
    else:
        inputs.append(sentense_maker(user_in))
        continue
