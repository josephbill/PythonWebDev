# Encapsulation : refers to bundling data and methods that work on the data in a single unit called class

class Employee:
    def __init__(self,name,salary):
        self.__name = name
        self.salary = int(salary)
        self.dateofreg = "10-31-2024"

    def display_employee(self):
        return f"Employee Name: {self.__name}, Salary: {self.salary} : {self.dateofreg}"

    def update_salary(self,amount):
        if amount > 0:
            self.salary += amount
        else:
            print("Salary cannot be negative")

# create an object
emp1 = Employee("Joseph","100000")
print(emp1.display_employee())
# print(emp1.__name)
emp1.__name = "Alice A"
print(emp1.update_salary(10000))
print(emp1.display_employee())

# __attributeName = private attribute / cannot be accessed nor modified after creation of the object