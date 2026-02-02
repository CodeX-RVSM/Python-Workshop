num=int(input("Enter a Number :"))
temp = num 
sum=0
while num>0:
    rem=num%10
    sum+=rem*rem*rem
    num//=10
if(temp==sum):
    print("Armstrong Number")
else:
    print("It is not Armstrong Num")