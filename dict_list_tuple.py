data={
    "student":{
        "id":123,
        "name":"sham",
        "marks":[12,34,23]

    }
}
print(data["student"]["marks"])

data["student"]["marks"][1]=24000
print(data["student"]["marks"])


institude={
    "branch":{
        "id":234,
        "name":"linkcode",
        "add":(101.000,123.000)
    }
}
print(institude["branch"]["add"])
