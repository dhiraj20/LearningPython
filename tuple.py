# fruits = ('Apple',)  If a tuple has single item, add comma ',' after an item.
# If comma is not added, it will become string
# fruits = ('Apple', 'Banana', 'Orange')
# print(fruits)

# Access / Read
# fruits = ('Apple', 'Banana', 'Orange')
# for item in fruits:
#     print(item)


# fruits = ('Apple', 'Banana', 'Orange', 'Apple', 'Banana', 'Apple')
# print('count', fruits.count('Apple'))
# print('index', fruits.index('Apple'))
# print('index of banana', fruits.index('Banana'))
# print('index of Orange', fruits.index('Orange'))

# print(fruits[2])

## + -> concatenation 
# summer_fruits = ('Mango', 'Watermelon')
# winter_fruits = ('Orange', 'Grapes')
# new_tuple = summer_fruits + winter_fruits
# print('summer_fruits', summer_fruits)
# print('winter_fruits', winter_fruits)
# print('new_tuple', new_tuple)

## * -> Repetition 
# summer_fruits = ('Mango', 'Watermelon')
# new_tuple = summer_fruits * 2
# print('winter_fruits', summer_fruits)
# print('new_tuple', new_tuple) #  ('Mango', 'Watermelon', 'Mango', 'Watermelon')

# fruits = ('Apple', 'Banana', 'Orange', 'Apple', 'Banana', 'Apple')
# print('Apple' in fruits)


## tuple comprehension 
# numbers = (1,2,3,4)
# new_tuple = tuple(item * 3 for item in numbers)
# print(new_tuple)

# numbers = (1,2,5,19,20,33,44)
# print("length of tuple", len(numbers))
# print("max of tuple", max(numbers))
# print("min of tuple", min(numbers))

# + concatenation -> add items of more than one tuples and return a single tuple
# tup1 = (1,6,9)
# tup2 = (2,7,22)
# tup3 = (3,0,19)
# new_tuple = tup1 + tup2 + tup3
# new_tuple2 = tup3 + tup1 + tup2
# print(tup1)
# print(tup2)
# print(tup3)
# print("new_tuple", new_tuple)
# print("new_tuple2", new_tuple2)

# * Repetition 
# tup1 = (1,6,9)
# new_tuple = tup1 * 3
# print(new_tuple)

# in Membership 
# numbers = (1,2,5,19,20,33,44)
# print(44 in numbers)
# isExists = 44 in numbers
# print(isExists)

## How can we modify tuple 
# Tuple --> List (After modification , add, remove, update) --> Tuple 
# districts = ('Morang', 'Jhapa', 'Illam')

# # 1. convert districts tuple to list
# district_list = list(districts) # [] or list()
# district_list.append("Panchthar")
# district_list.append("Taplejung")
# print(district_list)

# # Now convert list into tuple
# new_tuple = tuple(district_list)

# print("new_tuple", new_tuple)
# districts = new_tuple
# print("districts", districts)
# print(districts[3])



#Unpacking
# tup = ('Apple', 'Ball', 'Cat')
# first_value = tup[0]
# second_value = tup[1]
# third_value = tup[2]
# print(first_value)
# print(second_value)
# print(third_value)
# first_value, second_value, third_value = tup
# print(first_value)
# print(second_value)
# print(third_value)


# tup = ('Apple', 'Ball', 'Cat', 'Dog', 'Elephat', 'Fish', 'Giraffe', 'Horse', 'Iron', 'Jug')
# first, second, *values = tup
# print(first)
# print(second)
# print(values)

# tup = ('Apple', 'Ball', 'Cat', 'Dog', 'Elephat', 'Fish', 'Giraffe', 'Horse', 'Iron', 'Jug')
# first, second, *values, second_last, last = tup
# print(first)
# print(second)
# print(values)
# print(second_last)
# print(last)

# tup = ('Apple', 'Ball', 'Cat', 'Dog', 'Elephat', 'Fish', 'Giraffe', 'Horse', 'Iron', 'Jug')
# *values, second_last, last = tup
# print('values', values)
# print('second_last', second_last)
# print('last', last)

fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Papaya']
a,b,*e = fruits
print(a)
print(b)
print(e)