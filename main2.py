class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(f"Full Name: {self.fname} {self.lname}")
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year
    def display(self):
        self.printname()
        print(f"Graduation Year{self.year}")
fname = input("Enter first name: ")
lname = input("Engter last name: ")
year = input("Enter graduation year: ")
student1 = Student(fname, lname, year)
student1.display()