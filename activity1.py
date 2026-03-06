x = 8
if (type(x) is int):
    print("true")
else:
    print("false")

y = 8.2
if (type(y) is not float):
    print("true")
else:
    print("false")

a = 28
b = 28
if (a is b):
    print("x and y is same identity")

b = 10
if (a is not b):
    print("x and y don't have same idenity")