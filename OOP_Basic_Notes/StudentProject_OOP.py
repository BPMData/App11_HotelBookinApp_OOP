
class User:

    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        name = self.name.upper()
        return name

    def age(self, current_year):
        user_age = (current_year - self.birthyear)
        return user_age

user = User('John', 1999)

print(user.age(2023))

print(user.get_name())