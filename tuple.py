#tuple
#thistuple = ("car", "bus", "van")
#method

#1.index
#thistuple = (3,4,2,6,2,7,1)
#print(thistuple.index(3))

#2.convert a tuple into a list,change one value,append a new value,and again convert it into tuple
#thistuple = (3,4,2,6,2,7,1)
#thislist = list(thistuple)
#thislist[2] = 99
#thislist.append(10)
#newtuple = tuple(thislist)
#print(newtuple)

#3.to remove duplicate values from the list while keeping the original order
#original_list = [1,3,5,2,7,8,8,2]
#duplicate_list = list(dict.fromkeys(original_list))
#duplicate_list = list(set(original_list))
#print("ordered list without duplicates:",duplicate_list)

#4.to print only 'my' from the list 'apple is my fav'
#msg = 'apple is my fav'
#result = msg[9:11]
#print(result)

#5.reverse the string using slicing
#msg ='apple is my fav'
#result = msg[:: -1]
#print(result)

#6.to print the last character of a string
msg = 'apple is my fav'
#result = msg[-1]
result = msg[-3:]
print(result)

#7.to count how many time the values 2 appear in the list
#value = (3,4,2,6,4,4,1)
#result = value.count(4)
#print(result)

#8.to add a new item into a tuple
#msg = ['apple', 'is', 'my', 'fav'] 
#msg.append('fruit')
#print(msg)

#9.to find the length of a string without haedcoding the value
#msg = 'apple is my fav'
#result = len(msg)
#print(result)

#10.to print alternate character from a string
msg = 'apple is my fav'
result = msg[1::3]
print(result)