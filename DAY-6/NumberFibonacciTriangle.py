n=int(input("Enter the number of rows: "))
x,y=0,1
current=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(current,end=" ")
        current = x+y
        x,y = y,current
    print()