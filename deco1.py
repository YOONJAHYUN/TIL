class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')


class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    # def talk(self):
    #     print(f'반갑습니다. {self.name}입니다.')

    def study(self):
        self.gpa += 0.1

class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    # def talk(self):
    #     print(f'반갑습니다. {self.name}입니다.')

    # def teach(self):
    #     self.age += 1





p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

p1.talk()

s1.talk()