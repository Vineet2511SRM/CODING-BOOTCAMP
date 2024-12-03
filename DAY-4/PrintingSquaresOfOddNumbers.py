i=1  # Iterator for running the code for 'n' number of times
a=1  
n=int(input("Enter the number of terms to be printed: "))
while i<=n:
    if (a%4!=0):
        print(a**2)
        i+=1
    a+=1    