# To print first 'n' prime numbers without using functions

n=int(input("Enter the no. of prime numbers you want to print: "))
count=0
num=2
while count<n:
    isPrime=True
    for i in range(2, num):
        if num % i==0:
            isPrime=False
            break
    if isPrime:
        print(num, end=" ")
        count+=1
    num+=1
print()