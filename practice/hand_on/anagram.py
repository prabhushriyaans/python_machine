gram=[]
ls=[]
words = ["listen", "silent", "enlist", "google", "gogole", "cat", "act"]
for word in words:
    anagram=[]
    for subword in words:
        if sorted(word) == sorted(subword):
            anagram.append(subword)
    gram.append(anagram)

for lst in gram:
    if lst not in ls:
        ls.append(lst)
for anagrams in ls:
    print(anagrams)
 