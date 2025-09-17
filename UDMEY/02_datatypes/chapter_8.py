# Mutable

ingredients = ["Water","Milk","Black Tea"]

ingredients.append("Sugar")
print(f"Ingredients: {ingredients} ")

ingredients.remove("Sugar")
print(f"Ingredients: {ingredients} ")


spice_options =["Ginger","Cardamom"]
chai_ingredients = ["Water","Milk"]


chai_ingredients.extend(spice_options)
print(f"Chai Ingredients: {chai_ingredients}")
chai_ingredients.insert(2,"Black Tea")


last_Added = chai_ingredients.pop()
print(f"Last Added: {last_Added}")

chai_ingredients.reverse()
print(f"Chai Ingredients: {chai_ingredients}")

chai_ingredients.sort()
print(f"Chai Ingredients: {chai_ingredients}")


sugar_levels = [1, 2, 3, 4, 5]

print(f"Sugar Levels: {sugar_levels}")
print(f"Max Sugar Level: {max(sugar_levels)}")
print(f"Min Sugar Level: {min(sugar_levels)}")


base_liquid = ["Water", "Milk"]
extra_flavor   =["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Full Liquid Mix: {full_liquid_mix}")

strong_brew = ["Black Tea"]

print(f"Strong Brew: {strong_brew * 3}")


raw_spice_data= bytearray(b"CINAMON")
raw_spice_data = raw_spice_data.replace(b"CINA", b"CARD")
print(f"Raw Spice Data: {raw_spice_data}")