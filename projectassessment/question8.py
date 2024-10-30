
def get_day_week(day_number):
 # dictionary
    days = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }

    return days.get(int(day_number), "Invalid day number")

print(get_day_week(10))

dateselect = int(input("Enter a day number: "))
if dateselect == 1:
    print("monday")
elif dateselect == 2:
    print("tuesday")