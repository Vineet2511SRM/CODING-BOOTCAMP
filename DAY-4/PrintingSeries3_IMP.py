# 1,4,7,12,23,......

i=4
n = int(input("Enter the number of terms to be printed: "))
first,second,third = 1,4,7

if(n>=1):
    print(first,end="")
if(n>=2):
    print(",",second, sep="", end="")
if(n>=3):
    print(",",third, sep="", end="")

value = first + second + third
while i<=n:
    print(",",value, sep="", end="")
    first,second,third = second,third,value
    value = first + second + third
    i+=1
print("\b")  # Backspace tab