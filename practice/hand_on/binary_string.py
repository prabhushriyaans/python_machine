N=int(input("Enter the range of decimal numbers:"))
for i in range(1, N+1):
    bin_number = ""
    while i > 0:
        bin_number += str(i % 2)
        i //= 2
    print(bin_number[::-1],end=" ")
 