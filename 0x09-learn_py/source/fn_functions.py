def add(number_one: number, number_two: number) -> number:
    return number_one + number_two

def subtract(number_one, number_two):
    return number_one - number_two

def multiply(number_one, number_two):
    return number_one * number_two

def divide(number_one, number_two):
    if number_two == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    return number_one / number_two