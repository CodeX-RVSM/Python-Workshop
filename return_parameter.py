#without return type without parameters
def greet():
  print("hello")
greet()

#without return type with parameters
def get_number(n):
  print(n*n)
get_number(10)

#with return type parameters

def add(a,b):
  return a+b
print(add(10,20))
ans=add(10,20)
print(ans)

#with return type without parameters
def mul():
  return 2*2
print(mul()+2)
op=mul()
print(op+10*2)

# with return type with para by taking user IP
num=int(input("enter the number"));
def cube(num):
  return num*num*num
print(cube(num))
