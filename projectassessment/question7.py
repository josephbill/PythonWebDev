def triangle_type():
    a = float(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))

    # validation
    if a <= 0 or b <= 0 or c <= 0:
        return "sides must be positive"

    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"


print(triangle_type())