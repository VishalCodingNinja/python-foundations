# Employee is the same class as in 01_employee.py.
# Each file in this folder repeats the classes it needs, so it runs on its own.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def monthly_pay(self):
        return self.salary / 12


class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def hire(self, employee):
        self.employees.append(employee)

    def payroll(self):
        total = 0
        for e in self.employees:
            total += e.monthly_pay()
        return total


acme = Company("Acme")
acme.hire(Employee("Ana", 60000))
acme.hire(Employee("Raj", 48000))
print(acme.payroll())   # 9000.0
