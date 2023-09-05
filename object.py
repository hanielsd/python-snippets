# In Python, dictionaries are similar to objects in JavaScript. Here are some of the most commonly used methods for manipulating dictionaries in Python:


# The get() method returns the value of a specific key in a dictionary.
my_dict = {"name": "John", "age": 30}
value = my_dict.get("name")
print(value)  # Output: John


# The keys() method returns a list of all keys in a dictionary.
my_dict = {"name": "John", "age": 30}
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['name', 'age'])


# The values() method returns a list of all values in a dictionary.
my_dict = {"name": "John", "age": 30}
values = my_dict.values()
print(values)  # Output: dict_values(['John', 30])


# The items() method returns a list of all key-value pairs in a dictionary.
my_dict = {"name": "John", "age": 30}
items = my_dict.items()
print(items)  # Output: dict_items([('name', 'John'), ('age', 30)])


# The update() method updates the value of a specific key in a dictionary.
my_dict = {"name": "John", "age": 30}
my_dict.update({"age": 40})
print(my_dict)  # Output: {'name': 'John', 'age': 40}


# The pop() method removes and returns the value of a specific key in a dictionary.
my_dict = {"name": "John", "age": 30}
value = my_dict.pop("age")
print(value)  # Output: 30
print(my_dict)  # Output: {'name': 'John'}
