"""
Employee payro;ll system
add an employee and add a salary on the same
return total cost on payroll
"""

"""
{
  "salary" : ,
  "name" " , 
}
"""

"""
  [ 
    {
  "salary" : ,
  "name" " , 
}, 
{
  "salary" : ,
  "name" " , 
},

    
  ]
"""
employees = []

def add_employee(employees, name,salary):
    return employees + [{"name" : name, "salary" : salary}]

def calculate_total_payroll(employees):
    return sum(employee["salary"] for employee in employees if employee["salary"] > 0)

# usage
employees = add_employee(employees,"Joseph", 1000)
employees = add_employee(employees,"Habiba",2000)
total_payroll = calculate_total_payroll(employees)
print(total_payroll)
print(employees)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = int(salary)

class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self,employee):
        self.employees.append(employee)

    def total_payroll(self):
        return sum(employee.salary for employee in self.employees)

emp1 = Employee("Bob", "40000")
emp2 = Employee("Jane", "50000")
print(f"{emp1.name} {emp1.salary}")
payroll1 = Payroll()
payroll1.add_employee(emp1)
payroll1.add_employee(emp2)
print(f"Total Payroll {payroll1.total_payroll()}")

"""
How can we utilize the objects created from the class blueprint 
employee , to get the company's total payroll in class Payroll ? 
"""















