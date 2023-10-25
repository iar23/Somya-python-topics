fruits = ("apple", "banana", "cherry")
print(fruits[0])
print(fruits[1])
print(fruits[1:3])
print(len(fruits)) 
for fruit in fruits:
    print(fruit)
    if "banana" in fruits:
    print("Yes, 'banana' is in the fruits tuple")
    fruits2 = ("orange", "strawberry")
combined_fruits = fruits + fruits2
print(combined_fruits) 
count = fruits.count("cherry")
print(count) 