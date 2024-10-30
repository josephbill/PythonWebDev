"""
1. variable assignment , the info of what is stored and returned should be referenced in a variable
a,b
a = ?
b = ?
= assignment
2. Use the arithmetic operators to do the calculations
3. variable to store the result
"""
# # a = 4
# a = int(input("Enter value a : "))
# # b = 5
# b = int(input("Enter value b : "))
# result = 0
#
# # addition
# result = a + b
# print("The addition result is " , result)
# result = b - a
# print("The sub result is " , result)
# result = a * b
# print("The multi result is " , result)
# result = b / a
# print("The division result is " , result)


# in a function
def calculator():
    a = int(input("Enter value a : "))
    # b = 5
    b = int(input("Enter value b : "))
    operation = input("Enter operation : ")
    result = 0

    if operation == "+":
        result = a + b
        return result
    elif operation == "-":
        result = a - b
        return result
    elif operation == "*":
        result = a * b
        return result
    elif operation == "/":
        result = a / b
        return result


    # # addition
    # result = a + b
    # print("The addition result is ", result)
    # result = b - a
    # print("The sub result is ", result)
    # result = a * b
    # print("The multi result is ", result)
    # result = b / a
    # print("The division result is ", result)
    #
    # return result


print(calculator())


