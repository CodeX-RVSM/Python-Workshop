# syntax:lambna arguments:expression
x=lambda op:op*op*op
print(x(9))

power=lambda a,b:a**b
print(power(2,3))

x=lambda op:9*9*9
print(x)
print(x(10)) # Calling the lambda function with an argument'

python Scopes
L-locals
E-Enclosinf
G-Global
B-Built-in

def var():
  x=90
  x+98#modify localscope var
  print(x)

var()
# print(x) #---- nam 'x' is not defined

# another function
def other():
  var() #we can call function to another functions
  # x+=2  #but cannot access ocal variable'x'
  print(x)
other()
