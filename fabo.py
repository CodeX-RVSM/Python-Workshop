num=int(input("Enter a term"))
i=1
n1,n2=0,1
while i<=num:
    print(n1,end="")
    n1,n2=n2,n1+n2
    i+=1