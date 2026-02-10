y=[[1,2,3],[4,12,6],[7,8,9]]
# find the highest value using a for loop and a max variable
max_val = y[0][0] 
for i in y:
    for j in i:
        if j > max_val:
            max_val = j
print(f"max value : {max_val}")
