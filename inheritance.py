#inhertiance
#single inheritance
#one parent and one child
'''
class vegetable:
    def potato(self):
        print("potato is a fat")
class non_fat(vegetable):
    def tomato(self):
        print("tomato is not a fat")
d=non_fat()
d.potato()
d.tomato()
'''
class detial:
    def employee(self):
        print("Rohith Sankar")
class company(detial):
    def job(self):
        print("Working in Fatpipe")
s=company()
s.employee()
s.job()

#multiple inheritance
#many parent and one child
'''
class course:
    def BE(self):
        print("degree") 
class department:
    def ece(self):
        print("electronics and communication engineering")
class subject(course,department):
    pass
s = subject()
s.BE()
s.ece()
'''
#multilevel inhertiance
#grandparent-->parent-->child
'''
class grandfather:
    def house(self):
        print("grandfather's house")
class father(grandfather):
    def car(self):
        print("father's car")
class son(father):
    def bike(self):
        print("son's bike")
s=son()
s.house()
s.car()
s.bike()        
'''
#hierachial
#one parent and many child
'''
class company:#parent class
    def work(self):#both class inherits the work() method from company
        print("TCS company")
class employee(company):#child class
    def work(self):
        print("employee work in the company")
class manager(company):#child class
    def work(self):
        print("manager works in the company")
e=employee()
m=manager()
e.work()#both objects(e and m)can call work()
m.work()
'''
#hybrid inheritance
#combination of inheritance types

#base class
'''
class employee:
    def show_employee(self):
        print("I am an employee")
#derived class 1(hierachial inheritance)        
class manager(employee):
    def show_manager(self):
        print("I am a manager")
#derived class 2(hierachial inheritance)
class developer(employee):
    def show_developer(self):
        print("I am a developer")
#hybrid class(multiple inhertiance)
class teamlead(manager,developer):
    def show_teamlead(self):
        print("I am a teamlead")
t=teamlead()
t.show_employee()
t.show_manager()
t.show_developer()
t.show_teamlead()
'''        
                
                             
              
             