from employee import Employee
from inheritance import Manager
from payroll import Company


class Intern(Employee):
    def monthly_pay(self):
        return 1200  # flat stipend


acme = Company("Acme")
acme.hire(Employee("Ana", 60000))
acme.hire(Manager("Li", 90000, 12000))
acme.hire(Intern("Sam", 0))

for e in acme.employees:
    print(e.name, e.monthly_pay())
print("Total:", acme.payroll())   # Total: 14700.0
