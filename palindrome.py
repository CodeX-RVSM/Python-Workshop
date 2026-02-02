num=int(input("enter the number :"))
sum=0
temp=num
while num>0:
    rev=num%10

    sum=(sum*10)+rev

    num//=10
print("rev num is",sum)
if(temp==sum):
    print("it is pallandrome num")
else:
    print("not pallandrome")