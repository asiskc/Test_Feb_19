'''Q5. Define an Student class and initialize it with name and section. Now, make a classmethod that takes in a string parameter "name-A"
 which creates an instance and returns the instance based on parameter. [Hint: use @classmethod decorator]'''


class Student:
    def __init__(self,name, Section):
        self.name = name
        self.Section = Section


    @classmethod
    def getObjFromString(cls, inp):
        name, Section = inp.split("-")
        return cls(name, Section)

    def Display(self):
       print("Name is {} and section is {} ".format(self.name,self.Section))


    def setSection(self,Section):
        return marks

s=Student.getObjFromString('Aashish-B')
s.Display()
print(s.setSection(B))