fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Range Function
for i in range(5):
    print(i)


# For Loop with Index
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)
    

# In this example, we use the enumerate function to iterate over a list of fruits and their corresponding indices. The enumerate function returns a tuple containing the index and the value of each item in the list. We use tuple unpacking to assign these values to the variables i and fruit, and then print them to the console.