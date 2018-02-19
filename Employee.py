''' Create a Employee class and initialize it with first_name, last_name and salary.
 Also, it has a derived attribute called email, which is self generated when instance is created. Now, make methods to :
      a. Display - It should display all information of the employee instance.'''

class Employee:

    def __init__(self , First_name, Last_name , Salary):
        self.First_name=First_name
        self.Last_name=Last_name
        self.Salary = Salary

    @classmethod
    def getobjFromstring(cls,inp):
        First_name,Last_name,Salary= inp.split("-")
        return cls(First_name,Last_name,Salary)


    def printFirst_name(self):
        print(self.First_name)

    def printLast_name(self):
        print(self.Last_name)

    def printSalary(self):
        print(self.Salary)


s=Employee.getobjFromstring("aashish-KC-10000")
s.printFirst_name()
s.printLast_name()
s.printSalary()