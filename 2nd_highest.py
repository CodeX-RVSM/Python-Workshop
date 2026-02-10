y=[[1,2,3],[4,5,6],[7,8,9]]
print(y)
# [1,2,3,4,5,6,7,8,9]
x=[0]
for i in y:
  for j in i:
    x.append(j)
x.sort()
print(x[-1])
print(x[-2])
