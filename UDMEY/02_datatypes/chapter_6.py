# String

chai_type = "Ginger Tea"
customer_name = "Priya"

print(f"Customer {customer_name} ordered {chai_type} please !")

chai_description = "Aromatic and Bold"
print(f"Chai Description: {chai_description[0:8:1]}")
print(f"Chai Description: {chai_description[0:8:2]}")
print(f"Last Word: {chai_description[12:]}")
print(f"Last Word: {chai_description[::-1]}")


label_text = "Chai Special"
encoded_text = label_text.encode("utf-8")
print(f"Encoded Text: {encoded_text}")
