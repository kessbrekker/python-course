item = input("What item would you like buy? : ")
price = float(input(f"What is the {item} price? : "))
quanity = int(input(f"How many would you like {item} to {price} ? : "))
total = price * quanity

print(f"You bought {item} for ${total}")