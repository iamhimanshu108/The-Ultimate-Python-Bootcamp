flavours = ["Ginger", "Out of Stocks", "Lemon", "Cardamom", "Discontinued"]

for flavour in flavours:
    if flavour == "Out of Stocks":
        continue
    if flavour == "Discontinued":
        break
    print(f"Out Of Stocks")