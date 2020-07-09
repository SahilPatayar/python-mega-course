# Positive/Negative Indexes, Slicing


    Lists, strings, and tuples have a positive index system:
        ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            0      1      2      3      4      5      6
    And a negative indexsystem:
        ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            -7     -6     -5     -4     -3     -2     -1

    In a list, the 2nd, 3rd, and 4thitems can be accessed with:
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        days[1:4]
        Output: ['Tue', 'Wed', 'Thu']

    First three items of a list:
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        days[:3]
        Output:['Mon', 'Tue', 'Wed'] 

    Last three items of a list:
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        days[-3:]
        Output: ['Fri', 'Sat', 'Sun']

    Everything but the last:
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        days[:-1] 
        Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 

    Everything but the last two:
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        days[:-2] 
        Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 

    A single in a dictionarycan be accessed using its key:
        phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
        phone_numbers["Marry Simpsons"]
        Output: '+423998200919'


# List Comprehensions

    A list comprehension is an expression that creates a list by iterating over another container.

        Example: [i*2 for i in [1, 5, 10]]

        Output: [2, 10, 20]

    List comprehension with ifcondition:

        Example: [i*2 for i in [1, -2, 10] if i>0]

        Output: [2, 20]

    List comprehension with an ifandelsecondition:

        Example: [i*2 if i>0 else 0 for i in [1, -2, 10]]

        Output: [2, 0, 20]

# More on Functions

    Functions can have muliple parameters

    Function can have keyword or non-keyword parameters and Arguments can be passed as non-keyword(positional) arguments (e.g. a) or keywordarguments (e.g. b=2and c=10)

    An *args parameter allows the function to be called with an arbitrary number of non-keyword arguments
        Ex. def find_max(*args) - keeps all the arguments in a tuple

    An **kwargsparameter allows the function to be called with an arbitrary number of keyword arguments:
        Ex. def find_winner(**kwargs) - Keeps all the argument in a dict


    



