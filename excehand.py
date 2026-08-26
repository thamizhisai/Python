#try-->lets you test a block of code for errors
#except-->lets you handle the error
#else-->lets you execute code when there is no error
#finally-->lets you execute the code,regardless of the result of try and except blocks

#exception handling
#when an error occurs,or exception as we call it,python will normally stop and generate an error message.

#try and except
#try -> error?
#yes -> except runs ->finally
#No -> else runs -> finally
'''
try:
    print(x)
except:
    print("error occured")
'''
'''
try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("something else went wrong")
'''
#else
'''
try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")
'''
#finally
'''
try:
    print(x)
except:
    print("something went wrong")
finally:
    print("The 'try except' is finished")
'''
#try,except,else,finally
'''
try:
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    res = num1/num2
except ZeroDivisionError:
    print("error:cannot divide by zero!")
except ValueError:
    print("error:pls enter only numbers")
else:
    print("division successfully")
    print("res is:",res)
finally:
    print("program execution is completed.")
'''
 #Raise-->As a python developer you can choose to throw an exception if a condition occurs
 #to throw(or raise) an exception,use the raise keyword.

 #raise an error and stop the program if x is lower than 0

x  = 2
if x<0:
 raise Exception("sorry,no number below zero")
else:
 print("number is greater than zero")

    

