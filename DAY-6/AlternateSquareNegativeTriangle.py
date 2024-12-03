n=int(input("Enter the number of rows: "))
a=1
for i in range(1,n+1):
    for j in range(1,i+1):
        if a%4==0:
            a+=1
        if a%2==0:
            print(-a**2, end=" ")
        else:
            print(a**2, end=" ")
        a+=1
    print()