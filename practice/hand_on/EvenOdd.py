lst=list(map(int,input("Enter list elements:").split()))
result=[]
for i in lst:
    if i%2==0:
        result.append(i)
for i in lst:
    if i%2!=0:
        result.append(i)
print(f"Even numbers followed by odd numbers are :{result}")