# Employee is the same class as in 01_employee.py.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def monthly_pay(self):
        return self.salary / 12


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def monthly_pay(self):  # override
        base = super().monthly_pay()
        return base + self.bonus / 12


boss = Manager("Li", 90000, 12000)
print(boss.name)                     # Li, inherited from Employee
print(boss.monthly_pay())            # 8500.0
print(isinstance(boss, Employee))    # True
