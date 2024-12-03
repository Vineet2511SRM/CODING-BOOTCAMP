# Taking input from user
item_name=eval(input("Enter the item name: "))
unit_price=int(input("Enter the price of item: "))
quantity=int(input("Enter the quantity: "))
percentage_discount=float(input("Enter discount percentage: "))

# Calculating discount
total=unit_price*quantity
discount=(percentage_discount/100) * total
final=total-discount

# Printing the discount and final price
print("Total initial cost:",total)
print("Discount applied:",discount)
print("Final amount after discounting:",final)