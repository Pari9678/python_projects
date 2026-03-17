string = input("Enter your chosen string: ")
string2 = ("")
for i in string:
    string2 = i + string2
print ("The original string:", string)
print ("The reversed string:", string2)