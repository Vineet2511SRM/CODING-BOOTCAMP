item_code=input("Enter the code of the item: ")
item_name=input("Enter the name of the item: ")
quantity=int(input("Enter the quantity of the item: "))
price=float(input("Enter the price of the item: "))

final_price= price*quantity

print("-"*40)
print("%-15s: %-10s" %("Item Code", item_code))
print("%-15s: %-10s" %("Item Name", item_name))
print("%-15s: %-10s" %("Quantity", quantity))
print("%-15s: %-10s" %("Price of 1 item", price))
print("-"*40)
print("%-15s: %-10s" %("Final Price", final_price))
print("-"*40)