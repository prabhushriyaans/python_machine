lst=list(map(int,input().split()))
lst=set(lst)
lst=sorted(list(lst))
left=0
right=len(lst)-1
new_lst=[]
for i in range(len(lst)):
    if i%2==0:
        new_lst.append(lst[left])
        left+=1
    else:
        new_lst.append(lst[right])
        right-=1
print(new_lst)