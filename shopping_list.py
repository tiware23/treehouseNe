data = input("Fill the things that you want to keep! ")
list(data)
cart = []

for i in data:
    cart.extend(i)

print(cart)
