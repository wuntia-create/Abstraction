class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.idnumber}")
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)
        self.salary = salary
        self.post = post
name = input("Enter your name:")
idnumber = input("Enter your ID number: ")
salary = input("Enter your salary: ")
post = input("Enter your post: ")
emp = Employee(name, idnumber, salary, post)
emp.display()