cup = input("Choose Your Size (small/medium/large): ").lower()

if cup == "small":
    print("The price is $2.")
elif cup == "medium":
    print("The price is $3.")
elif cup == "large":
    print("The price is $4.")
else:
    print("Invalid size selected.")
