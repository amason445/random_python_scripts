"""
I implemented an option type from Scala in Python.
The below example function takes an arbitrary key and will check for it.
Depending on whether it exists or not, it will implement logic.
This allows modularity depending on whether the key exists or not.
It could be used to create a default key value pair if one is missing.
"""

def option(dictionary, key):
    if key in dictionary:
        print("Success. Key is in dictionary")
    else:
        print("Failure. Key is not in the dictrionary")

x = {"1": 1, "2":2}
y = {"2": 1, "3":2}

#should pass
test_1 = option(x, '1')
#should pass
test_2 = option(y, '3')
#should fail
test_3 = option(x, '3')
#should fail
test_4 = option(y, '1')
