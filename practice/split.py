N=int(input("Enter a number:"))
temp,r=0,0
temp=N
while temp>10:
    rev=1
    while temp>0:
        r=temp%10
        rev=rev*r
        temp=temp//10
    temp=rev
print(f"the minimum product of digits of {N}  such that product of digits < 10 is {temp}")