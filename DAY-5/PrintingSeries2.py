# Printing 2,3,7,14,24,37,53,72,94,........,n

n=int(input("Enter the number of terms to be printed: "))
difference=1
num=2
printed_count=1
index=1
while printed_count<=n:
    if index%3!=0:
        print(num, end=" ")
        printed_count+=1
    num+=difference
    difference+=3
    index+=1
print()