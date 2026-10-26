"""Module 6 · Class inheritance

A child class gets everything from its parent class, then adds or changes
what it needs. Here a Manager is an Employee with a bonus.

Run it:  python 06_classes/03_inheritance.py
"""


# Employee is the same class as in 01_employee.py.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def monthly_pay(self):
        return self.salary / 12


# Manager(Employee) means: Manager inherits from Employee
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        # super() is the parent class: let Employee set name and salary
        super().__init__(name, salary)
        self.bonus = bonus  # the one new attribute a Manager adds

    # Defining a method the parent already has replaces it for Managers.
    # This is called overriding.
    def monthly_pay(self):  # override
        base = super().monthly_pay()    # the normal Employee pay
        return base + self.bonus / 12   # plus a monthly share of the bonus


boss = Manager("Li", 90000, 12000)
print(boss.name)                     # Li, inherited from Employee
print(boss.monthly_pay())            # 8500.0: 7500.0 salary + 1000.0 bonus
print(isinstance(boss, Employee))    # True: a Manager is also an Employee
