print ("Half pyramid pattern of stars (*): ")
n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(1+n):
        print ("* ", end="")
    print ()