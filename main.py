class employee:
    def __init__(self, given_name, given_role, given_DoB):
        self.name = given_name
        self.role = given_role
        self.salary = 20000
        self.DoB = given_DoB
    def increase_salary(self):
        self.salary += 1000
    def calculate_age(self):
        2024 - self.DoB
class manager:
    def __init__(self, given_name, given_role, given_DoB, given_bonus):
        self.name = given_name
        self.role = given_role
        self.salary = 50000
        self.DoB = given_DoB
        self.bonus = given_bonus
        self.age = 2024 - self.DoB
    def calculate_age(self):
        2024 - self.DoB
    def increase_salary(self):
        self.salary += 1000
    def increase_bonus(self):
        self.bonus += 1000


