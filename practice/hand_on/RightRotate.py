L = [1, 2, 3, 4, 5, 6, 7]
k=int(input("Enter the number of rotations:"))
for i in range(k):
    temp=L.pop()
    L.insert(0,temp)
print(f"List after {k} right rotations is :{L}")