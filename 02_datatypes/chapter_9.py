# Sets

essential_spices = {"cardamom","ginger","cinnamon"}

optional_spices = {"saffron","nutmeg","clove","cinnamon"}

all_spices = essential_spices | optional_spices
print(f"All Spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"Common Spices: {common_spices}")


only_in_essential = essential_spices - optional_spices
print(f"Only in Essential Spices: {only_in_essential}")


print(f"Is Clove is in Essential Spices: {'clove' in essential_spices}  ")


