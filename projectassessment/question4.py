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
