a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

print("Before swapping values:", "a =", a, "b =", b, "c =", c)

a, b, c = b, c, a

print("After swapping values:", "a =", a, "b =", b, "c =", c)