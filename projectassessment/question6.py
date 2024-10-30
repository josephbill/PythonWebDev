def password_checker():
    user = input("Enter a password: ")

    if user == "python123":
        return "access granted"
    else:
        return "access denied"


print(password_checker())


