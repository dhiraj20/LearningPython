name = 'Anjana'

# print(name[1:4])
# print(text)


# print(name[0:4])

# print(name[-1])
# print(name[-2])

# print(name[-1:-5:-1])

# print(name[2:])
# print(name[::-1])

# print(name[:5])

# text = "My name is 'Anjana'. I live at Biratnagar"

# print(text[5])
# print(text[1:5])
# print(text[5:])
# print(text[:20])
# print(text[::-1])

## lower()
# text = "MY NAME IS DHIRAJ"
# print(text.lower())

## upper()
# text = "my name is dhiraj"
# print(text.upper())

## index()
# for word it returns the start index
# text = "My name is dhiraj"
# print('M', text.index('M'))
# print('a', text.index('a'))
# print('name', text.index('name'))
# print('dhiraj', text.index('dhiraj'))
# 

# isalnum() 
# alphabet or number or both
# text = 'abc1234'
# print(text.isalnum())

# isdigit
# text = '1234'
# print(text.isdigit())

# capitalize
# text = "my name is anjana"
# print(text.capitalize())

## strip 
# name = '  my name is Anjana  '
# print(name)
# # print(name.strip())
# # print(name.rstrip())
# print(name.lstrip())

# startswith
# text = "My name is anjana"
# print(text.startswith("M"))
# print(text.startswith("My"))
# print(text.startswith("My name"))
# print(text.startswith("my"))

# endswith
# text = "My name is anjana"
# print(text.endswith("anjana"))
# print(text.endswith("a"))
# print(text.endswith("ana"))
# print(text.endswith("jana"))
# print(text.endswith("aa"))

# join
# text = "My name is anjana"
# print('-'.join(text))
# print(','.join(text))

## title
# text = 'my name is anjana biratnagar'
# print(text.title())

## String formatting 

# format
# name = "Dhiraj"
# city = "Dharan"
# text = "My name is {}. I live at {}.".format(name, city)
# print(text)

# name = "ANjana"
# city = "Biratnagar"
# text = "My name is {}. I live at {}.".format(name, city)
# print(text)

# f-string 
# name = 'Anjana'
# city = 'Dharan'
# text = f"My name is {name}. I live at {city}"
# print(text)

name = 'anjana'
print(name.count('a'))
print(name.count('j'))
print(name.count('n'))