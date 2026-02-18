x=[[1,2,3],[4,5,3],[7,8,9]]

y = []
for i in x:
    sum = 0
    for j in i:
        sum += j
    y.append(sum)

print(y)
