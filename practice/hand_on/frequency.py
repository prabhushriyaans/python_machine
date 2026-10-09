from collections import Counter 
text=input("Enter a text: ")
text=text.split(" ")
freq=dict(Counter(text))
desc=sorted(freq.items(),key=lambda x:(-x[1],x[0]))
 
for key , frequency in desc:
    print(f"{key}:{frequency}")
    break