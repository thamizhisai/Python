#list
thislist = ["banana", "cherry", "apple"]
print(thislist)
#allow duplicate
thislist = ["apple", "cherry", "apple"]
print(thislist)
#find list length
thislist = ["apple", "banana", "mango"]
print(len(thislist))
#list() constructor to create new list
thislist = list(["apple", "banana", "mango"])
print(thislist)
#list by using index method
thislist = ["apple", "mango", "banana", "cherry", "grapes"]
#print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
#change the range of items
thislist = ["apple", "banana", "mango"]
thislist[0:1] = ["lemon", "grapes"]
print(thislist)
#insert
thislist = ["apple", "mango", "banana"]
#thislist.insert(2, "watermelon")
#append
#thislist.append("lemon")
#extend
#thislist.extend(["orange", "grapes"])
#remove
#thislist.remove("apple")
#pop()
#thislist.pop(1)
#delete
#del (thislist)[1]
print(thislist)


