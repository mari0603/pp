class Employee:
    def init(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
def get_salary_info(self):
    return f"Заробітна плата {self.name}: {self.salary}"

employee = Employee("Іван", "Інженер", 30000)
print(employee.get_salary_info())
