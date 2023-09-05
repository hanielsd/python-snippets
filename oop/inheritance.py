# Defining a Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)


# Defining a Child Class
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(self.name + " is studying")

"""
we define a class called Student that inherits from the Person class.
The Student class has three properties (name, age, and student_id) and one method (study).
We use the super() function to call the __init__ method of the parent class
to initialize the name and age properties.
"""

# Creating Objects
person = Person("John", 30)
student = Student("Jane", 20, "1234")

# Accessing properties
print("Hello, I am "+person.name+"..."+str(person.age)+" years old.")
print("Hello, I am "+student.name+"..."+str(student.age)+" years old. My student id is: "+student.student_id)

# calling methods
person.greet()
student.greet()
student.study()