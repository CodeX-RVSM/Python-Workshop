x=[[1,2,3],[4,5,3],[7,8,9]]
for i in range (len(x)):
  for j in range (len(x[i])):
    if x[i][j]==3:
      x[i][j]=6
print(x)
