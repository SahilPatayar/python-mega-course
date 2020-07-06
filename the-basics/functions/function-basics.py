#!/usr/bin/python3

def mean(value):

    if type(value) == dict or isinstance(value, dict):
        return sum(value.values()) / len(value)
    else:
        return sum(value) / len(value)

print(mean([10, 5, 5]))

print(mean({"Batman":9.0, "Superman":9.5, "Deadpool": 7.5}))