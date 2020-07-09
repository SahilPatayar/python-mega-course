#!/usr/bin/python3

# function with more than 1 argument

def volume(l, b, h):
    return l * b * h

print(volume(2,3,4))

###############################

# function (2a + b)

def cal(a, b):
    return 2*a + b

print(cal(2,1))

# call the cal function with keywords
print(cal(b=1, a=2))

###################################

# function with as many arguments

def printAll(*args):
    print("\n".join(args))

printAll("a", "b")

###################################

# function with no limited keyword arguments

def temperatures(**kargs):
    print(kargs)

temperatures(Mon= 90, Tue= 46, Wed= 34)



