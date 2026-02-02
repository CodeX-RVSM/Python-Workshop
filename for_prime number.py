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