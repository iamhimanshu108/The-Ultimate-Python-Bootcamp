#Dictionary

chai_order = dict(type="Masala Chai", size="Large", sugar=2)

print(f"Chai Order: {chai_order}")

chai_recipe = {}
chai_recipe["base"]= "Black tea"
chai_recipe["liquid"]= "Milk"


print(f"Chai Recipe: {chai_recipe['base']}")

print(f"Recipe: {chai_recipe}  ")

del chai_recipe["liquid"]
print(f"Chai Recipe after deletion: {chai_recipe} ")    

print(f"Is Sugar in the Order?{'sugar' in chai_order}")