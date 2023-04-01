#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if(username == 'admin' or username == 'ADMIN'):
        if(password == '12345'):
            return 'Access granted'
        else:
            return 'Access denied'
    else:
        return 'Access denied'
    pass

def hows_the_weather(temperature):
    # your code here
    if(temperature < 40):
        return "It's brisk out there!"
    elif(temperature > 40 and temperature < 65):
        return "It's a little chilly out there!"
    elif(temperature > 85):
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
    pass

def fizzbuzz(num):
    # your code here
    if(num % 3 == 0 and num % 5 == 0):
        return 'FizzBuzz'
    elif(num % 3 == 0):
        return 'Fizz'
    elif(num % 5 == 0):
        return 'Buzz'
    else:
        return num
    pass

def calculator(operation, num1, num2):
    # your code here
    if(operation == '+'):
        return num1 + num2
    elif(operation == '-'):
        return num1 - num2
    elif(operation == '*'):
        return num1 * num2
    elif(operation == '/'):
        return num1 / num2
    else:
        print('Invalid operation!')
        return None
    pass

# dog = 'cudly';

# if dog == 'hungry':
#     owner = 'refilling food bowls'
# elif dog == 'thirsty':
#     owner = 'refilling water bowl'
# elif dog == 'cudly':
#     owner = 'snuggling'
# else:
#     owner = 'reading'

# def control_flow(value):
#     if value:
#         print('yelp!')
#     else:
#         print('nope!')

# control_flow(False)
# control_flow(None)
# control_flow(True)
# control_flow('')
# control_flow(0)
# control_flow('0')


# ex = set((1, 2, 3))
# print(ex)

# age = 1

# is_baby = 'baby' if age < 2 else 'not a baby'
# print(is_baby)

# if age < 2:
#     is_baby = 'baby'
# else:
#     is_baby = 'not a baby'

# print(is_baby)

# def divide(num1, num2):
#     if(num1 != num2):
#         quotient = num1 / num2
#         print(quotient)
#     else:
#         print('an error occured')

# def divide(num1, num2):
#     try:
#         quotient = num1 / num2
#         print(quotient)
#     except ZeroDivisionError:
#         print('Error: num2 cannot be equal to 0')
#     except TypeError:
#         print('Error: input must be of type int or float')
#     finally:
#         print('isnt division fun')

# divide(5, 2)
# divide(5, 0)

# dog = 'cuddly'
# dict_map = {
#     'hungry': 'refilling food bowl',
#     'thirsty': 'refilling water bowl',
#     'playful': 'playing tug-of-war',
#     'cuddly': 'snuggling'
# }

# owner = dict_map.get(dog, 'reading')
# print(owner)