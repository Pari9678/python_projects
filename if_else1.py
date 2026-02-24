a = int(input("What's the purchasing cost?"))
b = int(input("What's the selling cost?"))

if a<b:
    profit = b-a
    print(f"Profit, {profit}")
else:
    loss = a-b
    print(f"Loss, {loss}")
