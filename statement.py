# if statement
'''
The if statement evaluates a condition. If the condition is true the code block
inside the if statement is executed, if the condition is false the code block
is skipped

Syntax:
    if condition:
        // code block
'''

# a = 10
# b = 20
# if a > b:
#     print('a is greater than b')
# else:
#     print('b is greater than a')

# week -> 1 -> Sunday, 2 -> Monday , 3 -> Tuesday

# day = 1
# if day == 1:
#     a = 3
#     b = 4
#     print('Sunday')
#     print('Sunday is the first day of week')
#     print('Sunday has been declared gov holiday in nepal')
#     print("sum", a + b)
#     # multiple lines of code block
# elif day == 2:
#     print('Monday')
#     print('Monday is the second day of week')
# elif day == 3:
#     print('Tuesday')
# elif day == 4:
#     print('Wednesday')
# elif day == 5:
#     print('Thursday')
# elif day == 6:
#     print('Friday')
# elif day == 7:
#     print('Saturday')
# else:
#     print('Invalid number. Please enter number between 1 to 7')


# Ternary operator
age = 17
# if age >= 18:
#     print('Vote')
# else:
#     print('You can not vote')

# print("Ternary operator")
# print('Vote') if age >= 18 else print('You can not vote')

# variable = true_value if condition else false_value
# result = 'Vote' if age >= 18 else 'You can not vote'
# print("result", result)

# a = 10
# b = 7
# result = a if a > b else b
# print(result)

# percentage = 20
# result = ''
# if percentage >= 80:
#     result = 'Distinction'
# elif percentage >= 60 and percentage < 80: # 60 - 79
#     result = 'First Division'
# elif percentage >= 50 and percentage < 60:
#     result = 'Second Division'
# elif percentage >= 35 and percentage < 50:
#      result = 'Third Division'
# else: 
#     result = 'Fail'

# print('The division is: ', result)


# a = 15
# b = 10
# add = a + b
# print("The sum of two number", add)
# print("The difference of tow number a and b: ", a - b)

age = 20
has_citizenship_card = False

if has_citizenship_card:
    if age >= 18:
        print("A person can give vote")
    else:
        print("A person can not give vote. He is under 18")
else:
     print("A person does not have citizenship card")

