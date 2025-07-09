a=2
b=3

print(a ** b) # 8
print(10%3) #1
print(13 / 2) #6.5
print(13 // 2) #6(roundup lower value)

userdetails ={
    "name": "John",
    "age": 30,
    "city": "New York"
} #dictionary

print(userdetails["name"]) # John
print(userdetails.get("age")) # 30
print(userdetails.get("country","USA")) # USA (default value if key not found)
print(userdetails.keys()) # dict_keys(['name', 'age', 'city'])
print(userdetails.values()) # dict_values(['John', 30, 'New York'])
print(userdetails.items()) # dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

userdetails["country"] = "USA" # add new key-value pair
print(userdetails) # {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}

userdetails["age"] = 31 # update existing key-value pair
print(userdetails) # {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}

del userdetails["city"] # delete key-value pair
print(userdetails) # {'name': 'John', 'age': 31, 'country': 'USA'}

userdetails.clear() # clear all key-value pairs
print(userdetails) # {}

userdetails = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print("name" in userdetails) # True
print("country" in userdetails) # False
print("city" not in userdetails) # False
print("country" not in userdetails) # True