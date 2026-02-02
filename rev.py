num=int(input("enter the number :"))
sum=0
while num>0:
    #last digit exact
    rev=num%10
    #sum
    sum=(sum*10)+rev
    #update
    num//=10
print("rev  num is ",sum)