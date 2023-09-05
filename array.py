# In Python, arrays are typically represented using lists. Here are some of the most commonly used methods for manipulating lists in Python:

# The append() method adds an item to the end of a list.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]


# The extend() method adds multiple items to the end of a list.
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]


# The insert() method adds an item to a specific position in a list.
my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # Output: [1, 4, 2, 3]


# The remove() method removes the first occurrence of an item from a list.
my_list = [1, 2, 3]
my_list.remove(2)
print(my_list)  # Output: [1, 3]


# The pop() method removes and returns the last item from a list.
my_list = [1, 2, 3]
item = my_list.pop()
print(item)  # Output: 3
print(my_list)  # Output: [1, 2]


# The index() method returns the index of the first occurrence of an item in a list.
my_list = [1, 2, 3]
index = my_list.index(2)
print(index)  # Output: 1


# The count() method returns the number of times an item appears in a list.
my_list = [1, 2, 3, 2]
count = my_list.count(2)
print(count)  # Output: 2


# The sort() method sorts the items in a list in ascending order.
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3]


# The reverse() method reverses the order of the items in a list.
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]
