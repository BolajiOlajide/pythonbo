"""
Lambda expressions or functions are simply anonymous functions that don't
really have a function name or the def keyword we used to define our
functions.
"""


def doubleX(x):
    return x * 2


# This can be rewritten as a lambda function as 👇
double = lambda x: x * 2

# Lambda functions are simple one-line functions that try
# to save you some space and time
print(double(2))
print(doubleX(2))
