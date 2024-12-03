# # eCommerce Problem Statement
# grand_total = 0
# total_quantity = 0

# # Level 2: Iterative Item Entry and Grand Total
# while True:
#     # Level 1: Basic Item Entry and Total Calculation
#     item_code = input("Enter the item code: ")
#     description = input("Enter the item description: ")
#     quantity = int(input("Enter the quantity: "))
#     price = float(input("Enter the price per unit: ")) 

#     # Calculate total for the item
#     item_total = quantity * price
#     print(f"Total for item {item_code} ({description}): ₹{item_total:.2f}")

#     # Update grand total and total quantity
#     grand_total += item_total
#     total_quantity += quantity 

#     # Ask user if they want to continue
#     more_items = input("Do you want to add another item? (y/n): ").lower() 

#     if more_items != 'y':
#         break

# # Display the grand total and total quantity
# print(f"\nGrand Total: ₹{grand_total:.2f}")
# print(f"Total Quantity: {total_quantity} units") 

# # Level 3: Applying Discounts
# if grand_total > 10000:
#     discount = grand_total * 0.10
#     grand_total -= discount
#     print(f"10% discount applied: ₹{discount:.2f}")
# if total_quantity > 20:
#     quantity_discount = grand_total * 0.05
#     grand_total -= quantity_discount
#     print(f"5% quantity discount applied: ₹{quantity_discount:.2f}") 

# #Level 4: Membership
# is_member = input('Are you a member? (y/n): ')
# if is_member == 'y':
#     member_discount = grand_total * 0.02
#     grand_total -= member_discount
#     print('Membership discount applied: ', member_discount)

# # Display the final total after discounts
# print(f"Final Grand Total after discounts: ₹{grand_total:.2f}")

#########################################################################################################################

n=int(input("Enter the number of items: "))
items=[]
grand_total=0
total_quantity=0

# Level 2
for i in range(n):
    print("\nEnter the details of item",str(i+1)+":\n")

    item_code=input("Enter the code of the item: ")
    item_name=input("Enter the name of the item: ")
    quantity=int(input("Enter the quantity of the item: "))
    price=float(input("Enter the price of the item: "))

    final_price= price*quantity
    grand_total+=final_price
    total_quantity+=quantity
    
    items.append([item_code, item_name, quantity, price, final_price])

print("-"*50)
for i in range(n):
    print("%-25s: %-10s" %("Item Code", items[i][0]))
    print("%-25s: %-10s" %("Item Name", items[i][1]))
    print("%-25s: %-10s" %("Quantity", items[i][2]))
    print("%-25s: %-10s" %("Price of 1 item", items[i][3]))
    print("%-25s: %-10s" %("Final Price", items[i][4]))
    print("-"*50)

print("%-25s: %-10s" %("Basic Grand Total", grand_total))
# Level 3
if grand_total>10000:
    grand_total=grand_total - (10/100)*grand_total

if total_quantity>20:
    grand_total=grand_total - (5/100)*grand_total

# Level 4
ch=input("Are you having a membership [y/n]: ")
if (ch.lower()=='y'):
    grand_total=grand_total - (2/100)*grand_total

# Level 5
if grand_total<5000:
    grand_total=grand_total + (5/100)*grand_total
elif grand_total>=5000 and grand_total<20000:
    grand_total=grand_total + (10/100)*grand_total
else:
    grand_total=grand_total + (15/100)*grand_total

print("-"*50)
print("%-25s: %-10s" %("Grand Total", grand_total))
print("-"*50)