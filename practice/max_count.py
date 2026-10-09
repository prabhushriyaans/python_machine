count_lst=[]
count=0
string=input()
string=string.replace("!"," ")
string=string.replace("?"," ")
string=string.replace("."," ")
lst=string.split(" ")
filtered_list=[]
word_count_list=[]
for i in lst:
    if i!='':
        filtered_list.append(i)
    count=0
    for ch in i:
        if ch.isalpha():
            count+=1
    count_lst.append(count)
    word_count_list.append([i,count])
print(filtered_list)
for word,c in word_count_list:
    if c==max(count_lst):
        print(f"{word}: {c}")