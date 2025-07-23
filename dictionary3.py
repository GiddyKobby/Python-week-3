#Make a dictionary

person = {
    "name": "Gideon",
    "age": 25,
    "country": "Ghana"
}

print(person)


#Access values

print("Name:", person["name"])
print("Age:", person["age"])
print("Country:", person["country"])


#Add or update values

person["age"] = 26  # update
person["email"] = "gideon@example.com"  # add new

print(person)


#Remove a key

del person["country"]
print(person)


#Loop through

for key in person:
    print(key, ":", person[key])


#Check if a key exists

if "email" in person:
    print("Email is:", person["email"])
else:
    print("No email yet")


# ✅ {} → make a dictionary
# ✅ key: value → store info
# ✅ dict["key"] → get/set
# ✅ del dict["key"] → delete
# ✅ in → check if key exists
# ✅ for key in dict → loop