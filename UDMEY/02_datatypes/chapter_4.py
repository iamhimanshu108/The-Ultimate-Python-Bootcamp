is_boiling = True
stri_count = 5  # Fixed spacing and removed semicolon

total_actions = stri_count + is_boiling  # True is treated as 1 in Python
print(f"Total actions {total_actions}")

milk_present = "Himanshu"
print(f"Milk present: {bool(milk_present)}")

water_hot = True
tea_added = False
can_serve = water_hot and tea_added  # Fixed variable name typo
print(f"Can serve tea: {can_serve}")  # Fixed typo in