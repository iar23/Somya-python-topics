person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New York"
}
print(person["first_name"])
print(person["age"])
person["age"] = 31
person["city"] = "San Francisco"
person["email"] = "john.doe@example.com"
del person["city"]
if "city" in person:
    print("City:", person["city"])
else:
    print("City not found in the dictionary")

    Rooms = {'totalroom' : 1000 ,'acroom' : 500 , 'nonac' : 500}
    print(Rooms['totalroom'])