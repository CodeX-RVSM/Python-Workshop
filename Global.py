# Gobal var = defined outside the function
x= 100

def test(y):
  global x
  print(x,y)

test(10)
