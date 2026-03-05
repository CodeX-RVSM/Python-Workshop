# loc var in nested fun
def outer():
  y=45
  def inner():
    nonlocal y
    print(y)
    y+=2
    print(y)
  inner()
  print(y)
outer()
