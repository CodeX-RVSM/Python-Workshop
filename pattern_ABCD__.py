n=3
i=0
ch=65
while i<n:
    j=0
    while j<=n:
        print(chr(ch), end=" ")
        ch+=1
        j+=1
    print(" ",i)
    i+=1

# A B C D   0
# E F G H   1
# I J K L   2