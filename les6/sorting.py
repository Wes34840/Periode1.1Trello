stuff = ['c',5645,9393.77,"hello", True, False, "Good morning",88, -90, 777.777, 90,665.33,"F"]


string = []
integer = []
floats = []
booleans = []

x = 0

while x < len(stuff):
    if type(stuff[x]) is str:
        string.append(stuff[x])
        x += 1
    elif type(stuff[x]) is int:
        integer.append(stuff[x])
        x += 1
    elif type(stuff[x]) is float:
        floats.append(stuff[x])
        x += 1
    elif type(stuff[x]) is bool:
        booleans.append(stuff[x])
        x += 1
    else:
        break

stuff.clear()
print(stuff)
print(string)
print(integer)
print(floats)
print(booleans)
