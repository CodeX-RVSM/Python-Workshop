# # reverse a number 
n= 65432
rev=0

for i in range(5):
    digit=n%10
    rev =rev*10+digit
    n=n//10
print('reverse of number is : ',rev)