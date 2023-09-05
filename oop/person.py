class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

person = Person("John", 30)
person.greet()  # Output: "Hello, my name is John"

print(person.name)
print(person.age)



"""
we define a class called Person with two properties (name and age) and one method (greet).
We use the __init__ method to initialize the properties when a new Person object is created.
"""