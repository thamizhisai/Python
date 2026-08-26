#pattern
'''
for i in range(1,6,2):
    print(i)
'''
'''
a = list(range(6))
print(a)
'''
#patterns
#1
#*
#**
#***
#****
#*****
'''
n=5
for i in range(1,n):
#for i in range(n-1,0,-1):#reverse
    for j in range(i):
        print("*",end = ' ')
    print()
'''
#1
#22
#333
#4444
#55555

n=5
for i in range(1,n+1):
   # print(str(i)*i)
    for j in range(i):
        print(i, end='')
    print()

#1
#12
#123
#1234
#12345
'''
n=5
for i in range(1,6):
#for i in range(5,0,-1)#reverse
    for j in range(1,i+1):
        print(j, end='')
    print()
'''
#A
#BC
#DEF
#GHIJ
'''
n=5
ascii_value = 65
for i in range(1,5):
    for j in range(i):
        print(chr(ascii_value),end='')
        ascii_value += 1
    print()
'''
#A
#AB
#ABC
#ABC
#ABCD

n=6
for i in range(1,6):
    ascii_value = 65
    for j in range(i):
        print(chr(ascii_value), end="")
        ascii_value += 1
    print()

#A
#BB
#CCC
#DDDD
'''
n=5
ascii_value = 65
#for i in range(1,5):
for i in range(4,0,-1):#reverse
    print(chr(ascii_value) * i)
    ascii_value += 1
print()
'''
#     *
#    **
#   *** 
#  ****
 #*****
n=5
#for i in range(1,n+1):
for i in range(5,0,-1):    
    print(" " * (n-i),end="") 
    print("*" * i)




