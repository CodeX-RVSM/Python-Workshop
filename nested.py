def fun1():
  x=56
  y=42
  def fun2():
    nonlocal x
    print(x)
    old_n=x
    print(x+y)
    x=89
    
    def fun3():
      nonlocal x
      print(old_n) #i want to print 56
      print(x+y)
    fun3()
  fun2()
fun1()
