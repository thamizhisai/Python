#if condtion
#warning on balance low
'''
balance = 300
if balance < 500:
    print("warning: low balance!")
'''
#18 above driving licence
'''
age = 20
if age >= 18:
    print("elegible for driving licence.")
'''
#above 1000 10% discount
'''
amount =1500
if amount >= 1000:
    print("10 percent discount.")
'''
#if else 
#pass or fail
'''
mark = int(input("Enter your mark: "))
if mark >= 35:
    print("pass the exam")
else:
    print("fail the exam")   
'''
#even or odd
'''
num = int(input("Enter the number: "))
if num % 2 == 0:
    print("even")
else:
    print("odd")
'''
#login success or failed
'''
username = input("Enter username: ") 
password = input("Enter password: ")
if username == "Thamizhisai" and password =="305202":
    print("login successfully")
else:
    print("login failed,please try again")   
'''
#elif
#Traffic signal
'''
signal = input("Enter the signal color: ")
if signal == "Red":
    print("stop")
elif signal == "yellow":
    print("Ready")
elif signal == "Green":
    print("Go")
else:
    print("invalid")
'''
#battery low
'''
battery = int(input("Enter the battery percentage: "))
if battery >= 80:
    print("battery full")
elif battery >= 50:
    print("battery medium")
elif battery >= 15:
    print("low power mode")
else:
    print("switch off")
'''
#movie ticket
'''
age = int(input("Enter your age: "))
if age < 5:
    print("Free ticket")
elif age <= 18:
    print("child ticket")
elif age <=60:
    print("adult ticket")
else:
    print("invalid option")
'''
#nested if
#cash withdrawal(Account & balance)
''' 
account = input("Enter the account status (active/inactive): ")
balance = int(input("Enter the balance amount: "))
if account == "active":
    if balance >= 1000:
        print("cash withdrawal sucessfully")
    else:
        print("insufficient balance")
else:
    print("account inactive")
'''
#online delivery availabilty(pincode&stock) 
'''
pincode = int(input("Enter your parcel pincode: "))
stock = input("Is item in stock? (yes/no): ")
if pincode == "614905":
    if stock == "yes":
        print("Delivery available")
    else:
        print("Item is out of stock")
else:
   print("delivery not available in your area")
'''
#grade
'''
grade = int(input("enter the number:= "))
if grade >= 90:
    print("A grade")
elif grade >= 89:
    print("B grade")
elif grade >= 79:
    print("C grade")
elif grade >= 60:
    print("D grade")
else:
    print("low grade")
'''
'''
grade = int(input("enter your grade: "))
if grade >= 90 and grade <= 100:
    print("A grade")
elif grade >= 70 and grade <= 89:
    print("B grade")
elif grade >= 50 and grade <= 69:
    print("C grade")
else:
    print("low grade")
'''
#truthy and falsy concept
a=(1,2,3,[4,5])
print(a[3])
a[3].extend([7,8])#a[3]+=[7,8] but tuple items cannot be changed
print(a)
