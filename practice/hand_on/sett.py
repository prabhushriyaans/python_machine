setA = {"apple", "banana", "cherry", "date"}
setB = {"banana", "date", "fig", "grape"}
outset=set()
setC=setA.intersection(setB)
for i in setA:
    if i not in setC:
        outset.add(i)
for i in setB:
    if i not in setC:
        outset.add(i)
print(f"Symmetric difference is :{outset}")