#Function
#syntax
#def function_name()
'''
def welcome():
    print("welcome to paris")
welcome()
'''
#four types of function
#1.function without argument and without return
#2.function with argument and without return
#3.function with argument and with return
#4.function without argument and with return

#1.function without argument and without return
'''
def Tamilnadu():
    print(" Tamilnadu is the best state for visiting")
Tamilnadu()
'''

#2.function with argument and without return
'''
def greet_user(username):
    print(f"Hello, {username}! welcome back.")
greet_user("Rohith")
'''
'''
def greet(b):
    print(f"hi {b}! how are you?")
name = "anu"
greet("priya")
greet(name)
'''
#3.function with argument and with return
#Addition
'''
def add(a,b):
    return(a+b)
#res=add(10,20)
#print(res)
print(add(10,20))
'''
#subraction
'''
def sub(a,b):
    return(a-b)
print(sub(100,25))
'''
#multiply
'''
def multiply(a,b):
    return(a*b)
print(multiply(16,16))
'''
#devision
'''
def div(a,b):
    return(a/b)
print(div(100,5))
'''
#4.function without argument and with return
'''
def square():
    num=5
    return num * num
result = square()
print(result)
'''
'''
def username():
    return "Thamizhisai"
res = username()
print(res)
'''
#1.Taking all remaining value and make it as tuble
'''
def stud_detial(name,*subject):
    print(name,subject)
stud_detial("Thamizhisai","Python","Java","c++")
'''
#2.Taking all remaining key value and make it as dic
'''
def stud_detial(name,**subject):
    print(name,subject)
stud_detial(" Thamizhisai",python=30,java=60,c=90)
'''
#3.example for both
'''
def stud_detial(name,*city,**subject):
    print(name,city,subject)
stud_detial("Thamizhisai","chennai","python",mark=70,result="pass")
'''
'''
def reg_detial(user_name,password,default_user = "user"):
    print(f"username {user_name},default_user {default_user}")
#reg_detial("tamil",123)
reg_detial("tamil",123,"vishwa")
'''
#task 2
#even list
'''
def even_list():
    a = [1,2,3,4,5]
    even = []
    for i in a:
        if i%2 == 0:
            even.append(i)
    return even
res = even_list()
print(res)
'''
#Task 2
#factorial
'''
def fact_value():
    num = 5
    fact = 1
    for i in range(1,num+1):
         fact = fact * i
    return fact
res = fact_value()
print(res)
'''
#task 4
#sorting
def sorted_list(arr):
    return sorted(arr)
num = [5,3,68,1,9,8]
res = sorted_list(num) 
print(res)    

