# Destructuring an Array
firstName, lastName = ["halefom", "alemu"]
print(firstName)  # Output: halefom
print(lastName)  # Output: alemu


# Destructuring an Object
person = {"name": "halefom", "age": 24}
name, age = person.values()
print(name)  # Output: halefom
print(age)  # Output: 24


# Destructuring an Object with Renaming
person = {"name": "halefom", "age": 24, "gender": "Male"}
name, age, sex = person["name"], person["age"], person["gender"]
print(name)  # Output: halefom
print(age)  # Output: 24
print(sex)  # Output: Male
