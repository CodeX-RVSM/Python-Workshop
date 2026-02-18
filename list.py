x=[[1,2,3],[4,5,6],[7,8,9]]
result=[]
for i in range (len(x)):
  sum=0
  for j in range(len(x[i])):
    sum+=x[j][i]
  result.append(sum)
print(result)
