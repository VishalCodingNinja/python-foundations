from employee import Employee


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


if __name__ == "__main__":
    acme = Company("Acme")
    acme.hire(Employee("Ana", 60000))
    acme.hire(Employee("Raj", 48000))
    print(acme.payroll())   # 9000.0
