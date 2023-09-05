# The split() method splits a string into a list of substrings based on a specified separator.
my_string = "Hello, World!"
words = my_string.split(", ")
print(words)  # Output: ['Hello', 'World!']


# The join() method joins the elements of a list into a single string, using a specified separator.
my_list = ["Hello", "World!"]
my_string = ", ".join(my_list)
print(my_string)  # Output: "Hello, World!"


# The replace() method replaces all occurrences of a specified substring with another substring.
my_string = "Hello, World!"
new_string = my_string.replace("World", "Python")
print(new_string)  # Output: "Hello, Python!"


# The lower() method converts all uppercase characters in a string to lowercase.
my_string = "Hello, World!"
new_string = my_string.lower()
print(new_string)  # Output: "hello, world!"


# The upper() method converts all lowercase characters in a string to uppercase.
my_string = "Hello, World!"
new_string = my_string.upper()
print(new_string)  # Output: "HELLO, WORLD!"


# The strip() method removes any leading and trailing whitespace characters from a string.
my_string = "   Hello, World!   "
new_string = my_string.strip()
print(new_string)  # Output: "Hello, World!"


# The startswith() method returns True if a string starts with a specified substring.
my_string = "Hello, World!"
result = my_string.startswith("Hello")
print(result)  # Output: True

# The endswith() method returns True if a string ends with a specified substring.
my_string = "Hello, World!"
result = my_string.endswith("World!")
print(result)  # Output: True

