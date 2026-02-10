y=[[1,2,3],[4,5,3],[7,8,9]]

# Create a new list 'x' by iterating through 'y' and replacing values
x = []
for row in y:
  new_row = []
  for item in row:
    if item == 3:
      new_row.append(6) # Replace 3 with 6
    else:
      new_row.append(item)
  x.append(new_row)

print(x)


# x=[[1,2,3],[4,5,3],[7,8,9]]
# for i in range (len(x)):
#   for j in range (len(x[i])):
#     if x[i][j]==3:
#       x[i][j]=6
# print(x)
