n=4
i=0
ch=97
while i<n:
    j=1
    while j<=i:
            print(chr(ch*i),end=" ")
            j+=1
    print("")
    i+=1

# 0 
# 1 0
# 0 1 0
# 1 0 1 0