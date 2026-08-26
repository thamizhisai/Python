#while loop
'''
i=1
while i<=9:
    print(i)
    i=i+1
'''
'''
i=1
while i<=5:
    print(i)
    i=i+2
'''    

#reverse
'''
i=5
while i>=1:
    print(i,end=",")
    i=i-1
'''
#reverse the number
'''
a=345
rev=0
while a>0:
    digit =a % 10
    rev =rev * 10 + digit
    a =a // 10
print(rev)
'''
#odd and even number in reverse
'''
i=9
while i>=1:
    print(i)
    i=i-2
'''
'''
i=10
while i>=2:
    print(i)
    i=i-2
'''
#for loops
#for i in range(5,0,-1):
'''
for i in range(1,20,2):
    print(i)
'''
#odd even by using for loop
'''
a = [2,3,4,5,6,7,8]
#even = []
odd = []
for i in a:
    if i % 2 != 0:
        odd.append(i)
       # even.append(i)
#print(even)
print(odd)
'''
#palindrome
'''
str1 = "madam"
rev = ''
for i in str1:
    rev = i + rev
if str1 == rev:
    print("palindrome")
else:
    print("not a palindrome")
'''
#anagram or not a anagram
'''
a = input("Enter the first string: ")
b = input("Enter the second string: ")
if len(a) == len(b):
    if sorted(a) == sorted(b):
        print("anagram")
    else:
        print("not a anagram")
else:
    print("length is different,so not a anagram")
    '''
#Break and continue
'''
for i in range(6):
    if i == 3:
        continue
       # break
    print(i)
'''
#while loop by using break
'''
i=0
while i < 6:
    if i==3:
        break
    print(i)
    i += 1
'''
#while loop by using continue
'''
i=0
while i< 6:
    i += 1
    if i == 3:
        continue
    print(i) 
'''   
'''
n=26
ascii_value = 65
for i in range(1,26):
    for j in range(i):
        print(chr(ascii_value),end='')
        ascii_value += 1
print()
'''

