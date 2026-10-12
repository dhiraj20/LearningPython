# create list

# fruits = [1,2,3, 'apple', 'ball', 'cat']
# print(type(fruits))
# print(fruits)

# fruits = list( ('Apple', 'Ball') )
# print(type(fruits))
# print(fruits)

# fruits = list()
# fruits = []

## Access
# To access single item from a list use 
# list[index]
# bag = ['brush', 'toothpaste', 'banana', 'water bottle', 'biscuit', 'comb']
# print(bag[0])
# print(bag[2])

## slicing / Slice
# slice => It will return a slice of items 
# list[startIndex, endIndex]
# startIndex should be smaller than endIndex

# print(bag[1:3])
# print(bag[1:]) # ['toothpaste', 'banana', 'water bottle', 'biscuit']
# print(bag[:4]) # ['brush', 'toothpaste', 'banana', 'water bottle']

# print(bag[0:4:2]) # step 2 , it will skip the 1 item
# print(bag[::3])
# print(bag[1::3])

# bag = ['brush', 'toothpaste', 'banana', 'water bottle', 'biscuit', 'comb']
# print(bag[-2])
# print(bag[-4: -1])


## Add
# bag = ['brush', 'toothpaste', 'banana', 'water bottle', 'biscuit', 'comb']

# append => It add value at the end of list
# bag.append('mirror')
# bag.append('shirt')
# bag.append('mobile')
# print(bag)


## insert(index, value) => It add value at the given index position 
# bag = ['brush', 'toothpaste', 'banana', 'water bottle', 'biscuit', 'comb']
# bag.insert(1, 'shirt')
# print(bag)
# bag.insert(2, 'mobile')
# print(bag)

## Update items 
## list[index] = value
# bag = ['brush', 'toothpaste', 'banana', 'water bottle', 'biscuit', 'comb']
# bag[1] = 'Mobile'
# print(bag)
# bag[3] = 'Coca Cola'
# print(bag)

# bag[1:3] = ['Coca Cola', 'Shirt', 'Mobile', 'Coca Cola', 'comb']
# print(bag)


## Remove 
# remove(value) --> It will remove an item from list
# bag = ['brush', 'toothpaste', 'banana', 'water bottle', 'biscuit', 'comb']
# bag.remove('banana')
# print(bag)
# bag.remove('biscuit')
# print(bag)

# pop()
# bag = ['brush', 'toothpaste', 'banana', 'water bottle', 'biscuit', 'comb']
# value = bag.pop()
# print(value)
# print(bag)

# pop(index)
# bag = ['brush', 'toothpaste', 'banana', 'water bottle', 'biscuit', 'comb']
# value = bag.pop(2)
# print(value)
# print(bag)


# index(value)
# bag = ['brush', 'toothpaste', 'banana', 'water bottle', 'biscuit', 'comb']
# value = bag.index('biscuit')
# print(value)

# count(value)
# bag = ['brush', 'toothpaste', 'banana', 'water bottle', 'banana', 'biscuit', 'comb', 'banana']
# value = bag.count('banana')
# print(value)

# numbers = [1,2,3,4,1,2,3,4,1,2,3,4]
# value = numbers.count(2)
# print(value)

# numbers = [1,2,3,4,1,2,3,4,1,2,3,4]
# min_value = min(numbers)
# max_value = max(numbers)
# print('min_value', min_value)
# print('max_value', max_value)

# bag = ['brush', 'toothpaste', 'banana', 'water bottle', 'banana', 'biscuit', 'comb', 'banana']
# min_value = min(bag)
# max_value = max(bag)
# print(min_value)
# print(max_value)

# extend --> It will modify the first list 
# list1 = [1,2,3]
# list2 = [5,6,7, 'apple']
# list1.extend(list2)
# print(list1) # [1, 2, 3, 5, 6, 7, 'apple']

## Concatenation '+', it will return new list 
# list1 = [1,2,3]
# list2 = [5,6,7, 'apple']
# list = list1 + list2
# print(list) # [1, 2, 3, 5, 6, 7, 'apple']
# print(list1)
# print(list2)


## Repetition 
fruits = ['Apple', 'ball']
print(fruits * 3) # ['Apple', 'ball', 'Apple', 'ball', 'Apple', 'ball']