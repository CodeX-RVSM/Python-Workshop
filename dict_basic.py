# s={
#     "name":"Rushi",
#     "age":21,
#     "add":"Pune"
# }
# print(s)
# print(s["name"])
# print(s["age"])


student={
    101:{"name":"rushi","age":21},
    102:{"name":"parth","age":20},
}
print(student)
print(student[101])
print(student[101]["name"])

# update
student[101]["name"]="Rushikesh"
print(student[101]["name"])
student[102]["age"]=22
print(student[102]["age"])
print(student)
print("-------------------")

for key in student:
  print(key)
print("--------------------")

for id,details in student.items():
  print(id)
  print("name :",details["name"])
  print("age :",details["age"])
  print()

student[103]={"name":"Atharva","age":18,"course Name":"python"}
print(student)
