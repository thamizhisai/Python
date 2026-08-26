#task 1
'''
class student:
    def __init__(self,name,course):
        self.name = name
        self.course =course
    def display(self):
        print("student name:", self.name)
        print("course:", self.course)
s1=student("Thamizhisai","python")
s1.display()
'''
#task 2
'''

class student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.total=student.sum_mark(mark1,mark2,mark3)
    @staticmethod
    def sum_mark(mark1, mark2, mark3):
        return mark1 + mark2 +mark3
    def display(self):
        print("student name:", self.name)
        print("total marks:", self.total)
s1 = student("Thamizhisai",mark1 = 80, mark2 = 70, mark3 = 75)  
s1.display()
''' 

#taks 3
'''
class fruit:
    fruit1 = "Apple"
    fruit2 = "Mango"
    fruit3 = "Banana"
    @classmethod
    def display_fruits(cls):
        print("fruit1:", cls.fruit1)
        print("fruit2:", cls.fruit2)
        print("fruit3:", cls.fruit3)
fruit.display_fruits()
'''
#class methods
class student:
    school = "London school"#class variable
    def __init__(self,name,mark):
        self.name = name#instance variable
        self.mark = mark#instance variable
    #instance method
    def display(self):
        print("name:", self.name)
        print("mark:", self.mark)
    #class method    
    @classmethod
    def show_school(cls):
        print("school:", cls.school)
    #ststic method
    @staticmethod
    def add(a,b):
        print("sum:",a+b)
#create object        
s1 = student("Ravi",85)
#call instance method
s1.display()
#call class method
student.show_school()
#call static method
student.add(10,20)




    


        