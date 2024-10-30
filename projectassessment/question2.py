"""
1. ask my user for the number to check
2. I need an operation to check if the number is odd or even
- modulo process to check division reminder , if 0 then its even , if not 0 is odd
"""
def oddeven_checker():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"The number {number} is even")
    elif number % 2 != 0:
        print(f"The number {number} is odd")

    return number

print(oddeven_checker())