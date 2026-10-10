from collections import Counter
l=int(input("Enter the max frequently  occuring numbers:"))
lst=[1,2,3,4,4,4,4,5,5,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,9,10,11,12,13,14,15,16,20,20,20]
dct=dict(Counter(lst))
ar=sorted(dct.items(),key=lambda x:(-x[1],x[0]))
for i in range(min(l,len(ar))):
    print(ar[i][0],end=" ")
# print(dct)
List=[]
while True:
    x=input("Enter the element:")
    if x==" ":
        break

    List.append(int(x))
List=list(filter(lambda x: x%2!=0 or x%2==0,map(int,input("Enter the elements:").split())))
lt2=list(map(lambda x:x**2,List))
for i in lt2:
    print(i,end=" ")
