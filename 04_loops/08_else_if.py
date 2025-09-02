staff = [("Amit",16), ("John",20), ("Sara",15), ("Dan",25)]

for name, age in staff:
    if age >=18:
        print(f"{name} is an adult")
        break
    else:
        print(f"{name} is not an adult")
