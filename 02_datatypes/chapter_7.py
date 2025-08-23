# Tuples

masala_spices = ("cardamon", "cloves", "cinnamon", "nutmeg")
(spice1, spice2, spice3, spice4) = masala_spices

print(f"Main Masala spices: {spice1}, {spice2}, {spice3}, {spice4}")


ginger_ratio, cadramon_ratio = 2,1

print(f"Ratio is G {ginger_ratio} : C {cadramon_ratio}")
ginger_ratio, cadramon_ratio = cadramon_ratio, ginger_ratio
print(f"New Ratio is G {ginger_ratio} : C {cadramon_ratio}")


# membership

print(f"Is Ginger in Masala spices ? {'Ginger' in masala_spices}")
