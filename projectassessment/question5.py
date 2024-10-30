def age_checker():
    age = int(input("Enter your age: "))

    if age < 0:
        return "Age cannot be negative"
    elif age < 18:
        return "You are a minor"
    elif age <= 65:
        return "You are an adult"
    else:
        return "You are a senior"

print(age_checker())