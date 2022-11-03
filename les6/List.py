def copy():
    mylist.append("Hello2")
    mylist.copy()

x = (3, 5)
y = ("Insert")

mylist = [10, "vijftig",10.25, 10]

print(mylist)

mylist.append("Hello")

print(mylist)

copy()

print(mylist)

count = mylist.count(10)
print(count)

mylist.extend(x)

print(mylist)

index = mylist.index(10.25)
print(index)

mylist.insert(3, y)

print(mylist)

mylist.pop(3)

print(mylist)

mylist.remove(10)

print(mylist)

mylist.reverse()

print(mylist)

mylist.clear()

print(mylist)

mylist.append("a")
mylist.append("z")
mylist.append("q")
mylist.append("t")
print(mylist)

mylist.sort()

print(mylist)
