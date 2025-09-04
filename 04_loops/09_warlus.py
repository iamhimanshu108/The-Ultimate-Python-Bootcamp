value = 13
remainder = value % 5

if remainder:
    print("Not Divisible the Remainder is:", remainder)


availabe_coins = [1, 5, 10, 25]
if (requested_size := input("Enter coin size: ")) in availabe_coins:
    print(f"Dispensing {requested_size} cent coin")
else:
    print("We don't have that coin size")



flavours = ["vanilla", "chocolate", "strawberry"]
if (requested_flavour := input("Enter flavour: ")) in flavours:
    print(f"Dispensing {requested_flavour}")
else:
    print("We don't have that flavour")