'''
def username(a, **b):
    print("a =",a)
    print("b =",b)
username(10,name="appe")
'''
'''
def sample_fun(a,b):
    print(a,b)
b=2
sample_fun("mm",b)
'''
#scope
#local variable
'''
def show():
    name = "apple"
    print(name)
show()
'''
#global variable
'''
name = ("apple")
def show():
    print(name)
show()
'''
#both global and local
'''
name = "apple"
def fun_name():
    name = "mango"
    print(name)
fun_name()
print(name)
'''
#lambda function --> ananymous function
#syntax --> argument : expression
'''
square_lambda = lambda x : x * x
print(square_lambda(5))
'''
#To find odd or even by using lambda
'''
a = [1,2,3,4,5]
res = list(map(lambda x : "even" if x%2==0 else "odd",a))
print(res)
'''
#map
#syntax --> list(map(fun,iterator))
'''
a = [1,2,3,4,5]
res = list(map(lambda i:i*2,a))
print(res)
'''
#filter
#syntax --> list(filter(fun,iterator))
'''
a=[1,2,3,4,5]
even=list(filter(lambda i:i%2==0,a))
print(even)
'''
#name using dict
'''
def stud_name(a):
    print(a['name'],a['marks'])
name ={"name":"Thamizhisai","marks":90}
stud_name(name)
'''
#generator
#yield-->send a value and pause the function
'''
def fun():
    x=10
    print(x)
    return
fun()
'''
'''
def numbers():
    yield 1
    yield 2
    yield 3
gen = numbers()
print(next(gen))
print(next(gen))
print(next(gen))
'''
'''
def count():
    for i in range(1,6):
        yield i
for number in count():
    print(number)    
'''
'''
def num():
    for i in range(1,1000001):
        yield i
for i in num():
     print(i)    
'''     