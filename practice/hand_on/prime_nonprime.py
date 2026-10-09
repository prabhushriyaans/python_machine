nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
primes=[]
Non_primes=[]
count=0
for i in nums:
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count<=2:
        primes.append(i)
    else:
        Non_primes.append(i)
# print(primes)
print(f"primes:",end=" ")
for i in primes:
    print(i,end=" ")
print(f"\nNon-primes:",end=" ")
for i in Non_primes:
    print(i,end=" ")