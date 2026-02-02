n=3
i=0
while i<n:
    j=1
    while j<=n:
        print(chr(65+i), end=" ")
        j+=1
    print("",i)
    i+=1

# A A A  0
# B B B  1
# C C C  2