from collections import Counter as C
st=input("enter a string :")
count=dict(C(st))
for i,ch in enumerate(st):
    if count[ch]==1:
        print(f"special charater:{ch} is present at {i}")