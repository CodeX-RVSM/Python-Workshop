s="INdIA"
print(s.swapcase())
print(s.startswith("nd"))
print(s.endswith("A"))
print(s.isalnum())
print(s.isupper())

a="ram"
b=23
print("my name is ",a,"my age is ",b)
print("my name {} my age is {}".format(a,b))
print("my name {a} my age is {b}")

s="InDia123"
#count a uppercase letters ,lowercase ,numbers,total length
up=low=dig=0
for i in s:
  if i.isupper():
    up+=1
  elif i.islower():
      low+=1
  elif i.isdigit():
        dig+=1
print("Uppercase Count is {up} "up,low,dig)

total_length = len(s)

print(total_length)

s="InDia123"
#count a uppercase letters ,lowercase ,numbers,total length
up=low=dig=0
for i in s:
  if i.isupper():
    up+=1
  elif i.islower():
      low+=1
  elif i.isdigit():
        dig+=1
print("Uppercase Count is {up} "up,low,dig)

total_length = len(s)

print(total_length)

fruit=["apper","mango","orange","kiwi","banana"]
print(fruit)
print(fruit[:3])
print(fruit[1:4])
fruit.append("Pineapple")
print(fruit)
fruit.insert(2,"grapes")
print(fruit)
anotherfruit=["cheery","Peru"]
print(fruit+anotherfruit)
fruit.extend(anotherfruit)
print(fruit)

#remove
s=["abc","pqr","Xyz"]
# print(s)
# s.pop()
# print(s)
# s.remove("abc")
# del s[0]
# del s;
# s.clear()
print(s)

# for i in range(1,len(s)):
  # print(s[i])
  
# while len(s)!=0:
#   s.pop()
# print(s)

while i<len(s):
  print(s[i])
  i+=1
