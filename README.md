# python-mega-course

# This repo contains lessions and code from course to learn python.


## The Basics

    1. Python has implicit variable declaration. Be careful when assiging the values to variables.
        x = 10   # here x is an integer
        y = '10' # here y is a str

    2. type(VARIABLE) can be used to find the type of variable.

    3. dir(type) gives the operations that can be performed on object of this type 
        Ex.: dir(str)

    4. help(type.method) to find help in using the operation
        Ex.: help(str.upper)

    5. dir(__builtins__) to show the python built in operations available

    6. Ctrl + L -> to clear screen on python shell

    7. exit() or Ctrl + Z to exit python interactive shell

    8. functions can be defined with def keyword and if they do not have explicit return statement then it returns None.


# Python data types

    1. List:
            Lists represent arrays of values that may change during the course of the program and can be created with square brackets.
            Ex.: list_of_daily_temps = [72.5, 79.8, 80.5]
    
    2. dict:
            dict is key value pair data type like hash map in java :) and can be created with curly brackets
            Ex. student_grades =  {"Batman":9.0, "Superman":9.5, "Deadpool": 7.5}
            
    3. tuple:
            tuples represent arrays of values that are not to be changed during the course of the program
            Ex. vowels = ('a', 'e', 'i', 'o', 'u')

