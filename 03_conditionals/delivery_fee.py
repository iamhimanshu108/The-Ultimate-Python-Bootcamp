order_amount = int(input("Enter the Order amount: "))

delivery_fee = 0 if order_amount >= 300 else 10

print(f"Delivery fee: ${delivery_fee}")
 
