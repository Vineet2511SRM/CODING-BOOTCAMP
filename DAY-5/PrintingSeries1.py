i=1
n=int(input("Enter number of terms to be printed: "))
for i in range(1,n+1):
    if(i%2==0):
        print(-2*i, end=" ")
    else:
        print(2*i, end=" ")
print("\b")