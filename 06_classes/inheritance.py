from employee import Employee


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def monthly_pay(self):  # override
        base = super().monthly_pay()
        return base + self.bonus / 12


if __name__ == "__main__":
    boss = Manager("Li", 90000, 12000)
    print(boss.name)                     # Li, inherited from Employee
    print(boss.monthly_pay())            # 8500.0
    print(isinstance(boss, Employee))    # True
