class Person:
    def __init__(self,name,id_number):
        self.name=name
        self.id_number=id_number
    def display(self):
        print("My name is ",self.name)
        print("My id number is : ",self.id_number)
class Employee(Person):
    def __init__(self, name, id_number,salary,post):
        self.salary=salary
        self.post=post
        Person.__init__(self,name,id_number)
child1=Employee("Tom",101,3000,"engineer")
child1.display()
