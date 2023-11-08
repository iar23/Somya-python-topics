employee_details={}
employee_details["employee1"] = {
    "name": "Somya Rai",
    "age": 25,
    "department": "HR"
}

employee_details["employee2"] = {
    "name": "Sakshi",
    "age": 29,
    "department": "Engineering"
}

employee_details["employee3"] = {
    "name": "Riya",
    "age": 35,
    "department": "Sales"
}
print(employee_details["employee1"]["name"]) 
for employee_id, details in employee_details.items():
    print(f"Employee ID: {employee_id}")
    print(f"Name: {details['name']}")
    print(f"Age: {details['age']}")
    print(f"Department: {details['department']}")
    print()



car_details = {
"car1": {
    "make": "Toyota",
    "model": "Camry",
    "year": 2022,
    "color": "Silver"
},
"car2": {
    "make": "Honda",
    "model": "Civic",
    "year": 2020,
    "color": "Blue"
},
"car3": {
    "make": "Ford",
    "model": "Escape",
    "year": 2021,
    "color": "Red"
}
}
for car_id, details in car_details.items():
    print(f"Car ID: {car_id}")
    print(f"Make: {details['make']}")
    print(f"Model: {details['model']}")
    print(f"Year: {details['year']}")
    print(f"Color: {details['color']}")
    print()