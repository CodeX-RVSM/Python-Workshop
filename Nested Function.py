#Function inside a function
def hello(name):
  print(f"Hello{name}")

def fav_city(city_name,name):
  hello(name)
  print(f"Welcome to{city_name}")

fav_city("Pune","Rushi")
