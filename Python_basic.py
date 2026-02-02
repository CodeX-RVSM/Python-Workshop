# #  print 1 to 10 numbers 
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print("\n-------print 1 to 10 numbers---------- ")

# #  print 10 to 1 numbers 
i=10
while i>=1:
    print(i, end=" ")
    i -=1    
print("\n-------print 10 to 1 numbers---------- ")

# # print first 10 even number 
i=2
while i<=21:
    print(i, end=" ")
    i +=2
print("\n-------print  first 10 even no ---------- ")

# # enter any no and print table 
n=6
i=1
while i<=10:
    print(f'{n} * {i} = {n*i}')
    i +=1

# # sum of first ten number     
i=1
sum=0
while i<=10:
    sum=sum+i
    i +=1
print(sum) 



# # factor of a given number 
n= int(input("enter a number to check factors  :"))
i=1
while(i<=n/2):
    if n%i==0:
        print(f'factor of {n} is {i}')
    i +=1


# # factorial  of a given number 
n= int(input("enter a number to check factorial :"))
i=1
fact =1
while(i<=n):
    fact =fact*i
    i +=1   
print(f'factorial of {n} is {fact}') 

# # fetch a digit
n =int(input("enter a number to fetch a digit :"))
while(n!=0):
    digit=n%10
    print(digit)
    n=n//10

# # fetch a even digit    
n=12357698
while(n!=0):
    digit=n%10
    if(digit%2==0):
        print(f'even digit {digit}')
    n=n//10    
# sum of even digit     
n=5647
sum=0
while(n!=0):
    digit=n%10
    if digit%2==0:
        sum=sum+digit
    n=n//10
print(f'sum of even digit is {sum}')    


# count digit
n=78543
count=0
while n!=0:
    n=n//10
    count+=1
print(f'count of digit is {count}')    


# # reverse a number 
n= 65432
rev=0
while n!=0:
    digit=n%10
    rev =rev*10+digit
    n=n//10
print(f'reverse of number is : {rev}') 


# palindrome number 
n =121
temp=n
rev=0
while n!=0:
    digit = n%10
    rev=rev*10+digit
    n=n//10
if temp==rev:
    print(f'number is pallindrome {temp}') 
else:
    print(f'number is not pallindrome {temp}')  



# prime number 
n=int(input("enter a number to check prime no :"))
i=2
is_prime =True

if n<=1:
    is_prime=False 
else:
    while i<=n//2:
        if n%i==0:
            is_prime=False 
            break
        i+=1
if is_prime:
     print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")  

# fibonacci series     
n=int(input("enter no fibo: "))
a=1
first=0 
second =1

while(a<=n):
    print( first, end=" ")
    third=first+second 
    first=second
    second =third
    a+=1

# ----------------armstrong number  
n = int(input(" \nEnter a number: "))
temp = n
count = 0
sum = 0

# Count number of digits

while temp != 0:
    count += 1
    temp //= 10

# Calculate sum of digits raised to power of count
temp = n
while temp != 0:
    digit = temp % 10
    sum += digit ** count
    temp //= 10

# Check Armstrong
if sum == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")