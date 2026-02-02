n=4
i=1
while i<=n:
    j=1
    while j<=i:
            if(i+j)%2==0:
                print("1",end=" ")
            else:
                print("0",end=" ")
            j+=1
    print("")
    i+=1

# 1 
# 0 1
# 1 0 1
# 0 1 0 1