class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def monthly_pay(self):
        return self.salary / 12


ana = Employee("Ana", 60000)
raj = Employee("Raj", 48000)
print(ana.name)             # Ana
print(ana.monthly_pay())    # 5000.0
print(raj.monthly_pay())    # 4000.0
