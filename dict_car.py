# car  ---- modelno(name,price,color)
car={}
ip=int(input("enter the number of cars : "))
for i in range(ip):
  model_no=int(input("enter the model no : "))
  name=input("enter the car name : ")
  price=int(input("enter the price : "))
  color=input("enter the color : ")
  car[model_no]={"name":name,"price":price,"color":color}
print(car)
print("color",car[model_no]["color"])
