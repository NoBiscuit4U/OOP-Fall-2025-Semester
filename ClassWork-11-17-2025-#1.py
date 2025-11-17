class Person:
    def __init__(self,name,dob,gg):
        self.name=name
        self.dob=dob
        self.gg=gg

    def display(self):
        print("    Personal Information: ")
        print(f"        Name: {self.name}")
        print(f"        DateOfBirth: {self.dob}")
        print(f"        Gender: {self.gg}")

class Student(Person):
    def __init__(self,name,dob,gg,major,id):
        Person.__init__(self,name,dob,gg)
        self.major=major
        self.id=id

    def display(self):
        print("-------------------")
        print("Student Information: ")
        print(f"    Major: {self.major}")
        print(f"    ID: {self.id}")
        Person.display(self)

class Faculty(Person):
    def __init__(self,name,dob,gg,desig,salary):
        Person.__init__(self,name,dob,gg)
        self.desig=desig
        self.salary=salary

    def display(self,test=""):
        print("-------------------")
        print("Faculty Information: ")
        print(f"    Designation: {self.desig}")
        print(f"    Salary: {self.salary}")
        Person.display(self)
        if test!="":
            print(f"    Test: {test}")

stu1=Student("John","1999","Male","CS","123")
stu1.display()

fac1=Faculty("Tim","1979","Male","Professor","$100,000")
fac1.display("test")
