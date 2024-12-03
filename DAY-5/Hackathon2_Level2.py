n=int(input("Enter the number of items: "))
items=[]
grand_total=0
for i in range(n):
    print("Enter the details of item",str(i+1)+":")

    item_code=input("Enter the code of the item: ")
    item_name=input("Enter the name of the item: ")
    quantity=int(input("Enter the quantity of the item: "))
    price=float(input("Enter the price of the item: "))

    final_price= price*quantity
    grand_total+=final_price
    
    items.append([item_code, item_name, quantity, price, final_price])

print("-"*50)
for i in range(n):
    print("%-25s: %-10s" %("Item Code", items[i][0]))
    print("%-25s: %-10s" %("Item Name", items[i][1]))
    print("%-25s: %-10s" %("Quantity", items[i][2]))
    print("%-25s: %-10s" %("Price of 1 item", items[i][3]))
    print("%-25s: %-10s" %("Final Price", items[i][4]))
    print("-"*50)

print("%-25s: %-10s" %("Grand Total", grand_total))
print("-"*50)