# Сотрудник и менеджер
class Employee:
    def __init__(self, name,salary):
        self.name=name
        self.salary=salary
    def get_payment(self):
        return print(f'{self.salary}')
class Manager(Employee):
    def __init__(self, name ,salary,bonus):
        super().__init__(name,salary)
        self.bonus=bonus
    def get_payment(self):
        return print(f'{self.salary+self.bonus}')
dev=Employee('Timur',15000)
manager=Manager('anna',17000,2000)
manager.get_payment()
dev.get_payment()