'''
    Instead of writing many if...elif statement you can use match statement
    Syntax:
        match expression:
            case X:
                // code block
            case Y:
                // code block
            case _:
                // default code block
'''
# day = 71

# match day:
#     case 1:
#         print('Sunday')
#     case 2:
#         print('Monday')
#     case 3:
#         print('Tuesday')
#     case 4:
#         print('Wednesday')
#     case 5:
#         print('Thursday')
#     case 6:
#         print('Friday')
#     case 7:
#         print('Saturday')
#     case _: # default, if none of the case matches then this will execute
#         print('Invalid number. Please enter number between 1 to 7')
    
day = 'sunday'

match day:
    case 'sunday':
        print("1. First day of week")
    case 'monday':
        print("2. Second day of week")
    case _:
        print("Invalid input")