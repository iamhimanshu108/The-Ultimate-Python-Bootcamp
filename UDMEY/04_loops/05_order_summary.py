names = ["Hitesh","Himanshu","Jitu", "Pankaj"]

bills = [50,70,100,130]

for names, amount in zip(names, bills):
    print(f"{names} paid {amount}")