# What is a function?
# fucntions are reusable blocks of code
# so far we have used print, len, str,
# syntax: def, name of function followed by() and open it up with:
#
# # create a function to greet
# def greeting():
#     return "hello world"
# # this is how we print a function
# print(greeting())
#     # pass is used to skip the function
#     # pass is used in creating or building a unit test

# def model():
#     return "macbook air"
# print(model())
#
# def tool():
#     return "screwdriver"
# print(tool())

# methods with parameters/ arguments
# function below returns + operation on values given
# def add_values(num1, num2):
#     return num1 + num2
# print(add_values(4, 9))
#
# #  function below returns multiplication
# def multiply_vals(num3, num4):
#     return num3 * num4
# print(multiply_vals(7, 6))
#
# # create a function with two args to return a subtraction of the 2 values given
# def num_sub(num5, num6):
#     return num5 - num6
# print(num_sub(23, 9))
#
# # create a function with two args to return a division of the 2 values given
# def num_div(num1, num2):
#     return num1 / num2
# print(num_div(8, 2))
#
# # create a function with two args to return a remainder of  of the 2 values given
# def num_mod(num1, num2):
#     return num1 % num2
# print(num_mod(6, 37))

# input experiment


# create a function with multiple args

def multi_args(*multiargs):

    for args in multiargs:
        print(args)
    return args
print(multi_args(1, 2, 2, 3, 3, 4, 4, 5))


