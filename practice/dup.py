st=input("Enter a string:")
st=st.lower()
stt=set()
dups_ch=set()
lst=[]
for i in st:
    if i not in stt:
        lst.append(i)
        stt.add(i)
    else:
        dups_ch.add(i)
print("".join(lst))
print(f"Duplicate characters:{",".join(list(dups_ch))}")