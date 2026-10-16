# Create

# person = {'name': 'Anjana', 'address': 'Brt', 'name': 'Dhiraj'}
# person = dict(name='Anjana', address='Brt')
# print(person)

# Add
# person = {}
# person['name'] = "Dhiraj"
# person['address'] = "Biratnagar"
# print(person)

# fromkeys(keys, value) , keys => list, It will add same value to all keys
# keys = list of items ['x','y','z']
# value = a value [number or string or list or tuple]

# keys = ['x', 'y', 'z']
# values = dict.fromkeys(keys, 'Apple') # It returns dict 
# print(values)

# setdefault 
# person = {'name': 'Anjana', 'address': 'Brt'}
# print(person)
# person.setdefault('salary', 25000)
# person.setdefault('address', "Dharan")
# print(person)

## Access value with [key]
# person = {'name': 'Anjana', 'address': 'Brt', 'salary': 25000}
# name = person['name']
# address = person['address']
# print(name)
# print(address)
# person['education'] education key is not present in above dict, it will give KeyError

## Access value with get(key, [defaultValue])
# If key is not present it returns None, if we add defaultValue then it will return defaultValue
# if key is not present in dict, it will return the defaultValue
# person = {'name': 'Anjana', 'address': 'Brt', 'salary': 25000}
# name = person.get('name')
# address = person.get('address', 'Dharan')
# salary = person.get('education', 'Add Education')
# print(name)
# print(address)
# print(salary)


## keys, values and items
# person = {
#     'name': 'Anjana', 
#     'address': 'Brt', 
#     'salary': 25000
# }
# keys = person.keys()
# values = person.values()
# items = person.items()
# print('Keys', keys) # Keys dict_keys(['name', 'address', 'salary'])
# print('values', values) # values dict_values(['Anjana', 'Brt', 25000])
# print('items', items) # dict_items( [ ('name', 'Anjana'), ('address', 'Brt'), ('salary', 25000) ] )

# for a,b in items:
#     print(a,b)

# for item in values:
#     print(item)


# Remove 
# person = {
#     'name': 'Anjana', 
#     'address': 'Brt', 
#     'salary': 25000
# } 
# print(person)
# # del person['education']
# #value = person.pop('education', 'Key not present')
# print(value)
# print(person)


# popitem() -> it will remove the last key-value pair
# person = {
#     'name': 'Anjana', 
#     'address': 'Brt', 
#     'salary': 25000,
#     'education': 'BE'
# } 
# print(person)
# value = person.popitem()
# print(value)
# print(person)

# Update [key]
# person = {
#     'name': 'Anjana', 
#     'address': 'Brt', 
#     'salary': 25000,
#     'education': 'BE'
# } 
# print(person)
# person['name'] = "dhiraj"
# person['salary'] = 30000
# print(person)

# person = {
#     'name': 'Anjana', 
#     'address': 'Brt', 
#     'salary': 25000,
#     'education': 'BE'
# } 
# print(person)
# person.update({'name': 'Dhiraj', 'salary': 3000, 'education': 'Master', 'job': 'Yes', 'Gender': 'Male'})
# print(person)


person = {
    'name': 'Anjana', 
    'address': 'Brt', 
    'salary': '25000',
    'education': 'BE'
} 
len = len(person)
# min = min(person)
# max = max(person)
max_values = max(person.values())
print(len)
# print(min)
# print(max)
print(max_values)

numbers = {item: item * 3 for item in range(6) }
print(numbers)