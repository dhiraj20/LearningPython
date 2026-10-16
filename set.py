# numbers = {1,2,3,4,5, 1,2,3,4,5,1,1,2,2,3}
# print(type(numbers))
# print(numbers)

# lst = ['Apple', 'Banana', 'Orange', 'Apple', 'Banana', 'Orange', 'Apple', 'Banana', 'Orange', 'Grapes']
# fruits = {'Apple', 'Banana', 'Orange', 'Apple', 'Banana', 'Orange', 'Apple', 'Banana', 'Orange', 'Grapes'}
# print("fruit set", fruits)
# print("list", lst)

# names = {'Dhiraj', 'Dhiraj'}
# print(names)

# Empty set
# fruits = {}
# fruits = set()

# Add an item to set -> add(value)
# fruits = set()
# fruits.add("Apple")
# fruits.add("Banana")
# fruits.add("Grapes")
# fruits.add("Apple")
# fruits.add("Banana")
# fruits.add("Papaya")
# print(fruits)


# Remove an item form set --> 
# It an item is not found it will throw KeyError

# 1. remove(value)
# fruits = {"Apple", "Ball", "Cat", "Dog"}
# print(fruits)
# fruits.remove("Ball")
# fruits.remove("Fish")
# print(fruits)

# 2. discard(value) -> it will remove an item in found, it not found it will not throw error
# fruits = {"Apple", "Ball", "Cat", "Dog"}
# print(fruits)
# fruits.remove("Ball")
# fruits.discard("Fish")
# print(fruits)

# 3. pop() -> It will remove an item form set, and it returns the value
# fruits = {"Apple", "Ball", "Cat", "Dog"}
# print(fruits)
# value = fruits.pop()
# print(fruits)
# print(value)

# fruits = {"Apple", "Ball", "Cat", "Dog"}
# value = fruits.pop()
# print(value)
# print(fruits)

# clear() -> It removes all values form a set 
# fruits = {"Apple", "Ball", "Cat", "Dog"}
# print(fruits)
# fruits.clear()
# print(fruits)

# Access an item 
# fruits = {"Apple", "Ball", "Cat", "Dog", "Egg"}
# for item in fruits:
#     print(item)

# print(len(fruits))


# Set operations 

# A = {1,2,3,4,5}
# B = {3,5,6,7,8,9}

# union = A | B
# union = A.union(B)
# print(union)

# intersection = A & B
# intersection = A.intersection(B)
# print(intersection)

# difference A - B
# diff = A - B
# diff = B.difference(A) # B - A
# print(diff)

# A = {1,2,3,4,5}
# B = {3,5,6,7,8,9}
# symmetric_difference A ^ b
# symm_diff = A ^ B
# symm_diff = A.symmetric_difference(B)
# print(symm_diff)
# print(A)
# print(B)

A = {1,2,3,4,5}
B = {3,5,6,7,8,9}

# A = A | B
# A.update(B) # A = A | B
# print("A values", A)
# print("B values", B)

# A = A - B # It will calculate difference and assign it to A
# A.difference_update(B)
# print("A values", A)
# print("B values", B)

# A = {1,2, 3 ,4, 5 }
# B = {3,5,  6,7,8,9}
# A.symmetric_difference_update(B) # A = A ^ B
# print("A values", A)
# print("B values", B)

# Set comprehension 
A = {1,2,3,4}

# new_set = { item* 2 for item in A }
new_set = { item* 2 for item in A if item > 2} #{2,4,6,8
print(new_set)