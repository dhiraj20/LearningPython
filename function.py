# sum 
# a = 10 
# b = 20
# sum = a + b # + operator 
# print(sum)

# # 30, 40
# x = 30
# y = 40
# sum = x + y
# print(sum)

# 100, 250
# a = 110 
# b = 210
# sum = a + b
# print(sum)


## Define a function 

# def sum(a,b):
#     sum = a + b
#     print(f"Sum of {a} and {b} = ", sum)
#     return sum

# s = sum(20,10)
# print("s value", s)
# sum(30,40)
# sum(100, 250)


# def subtract(a,b):
#     sub = a - b
#     return sub;

# x = 100
# y = 40
# value = subtract(x, y)
# print(value)

# x = 200
# y = 150
# value = subtract(x,y)
# print(value)


## Default parameter
# def sum(a = 10,b = 20):
#     sum = a + b
#     print(sum)

# sum(10)
# sum(20, 100)
# sum()


# def sum(a,b,c = 30,d = 30,e = 20):
#     sum = a + b + c + d + e
#     print(sum)

# sum(10,20, 5)

# def sum(a,b,c):
#     sum = a + b + c
#     print(sum)
#     print("a", a)
#     print("b", b)
#     print("c", c)

# sum(1,3,5)

# sum(5,3,1)

# sum(c=5, b=3, a=1)

# def sum(a,b,c, /, d):
#     sum = a + b + c + d
#     print(sum)
# sum(3,1,5, d=2)


# first_name = "Anjana"
# last_name = "Kangoi"
# Anjana Kangoi

## Keyword only arguments
# def sum(*,a,b):
#     print(a,b)

# sum(a=20,b=10)



# def get_name(*, first_name, last_name):
#     name = f'{first_name} {last_name}'
#     print(name)

# get_name(last_name="Kangoi", first_name = "Anjana") # Keyword
# get_name(first_name="Anjana", last_name = "Kangoi") 


# before '/' all becomes positional only argument
# After '*' all becomes keyword only argument
def sum(a,b,c, /,d, e, *,f,g):
    print(a,b,c,d,e,f,g)

sum(10,20,30, 40, 50, f=40, g=70)