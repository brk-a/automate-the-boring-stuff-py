#!/usr/bin/env python3

import sys


def calc(first, op, second):
    match op:
        case '+':
            print(f'{first} {op} {second} = {first + second}') 
        case '-':
            print(f'{first} {op} {second} = {first - second}') 
        case '*':
            print(f'{first} {op} {second} = {first * second}') 
        case '/':
            print(f'{first} {op} {second} = {first / second if second != 0 else "is not allowed"}')
        case '%':
            print(f'{first} {op} {second} = {first % second if second != 0 else "is not allowed"}')
        case '//':
            print(f'{first} {op} {second} = {first // second if second != 0 else "is not allowed"}')
        case _:
            print(f'{op} is not allowed on this calculator')
            print(f'Usage 1: ./2-calculator num1 op num2')
            print(f'Usage 2: python3 2-calculator.py')

if __name__ == '__main__':
    if len(sys.argv) != 4:
        first = float(input('Enter num ...\n'))
        op = input('Enter operator ...\n')
        second = float(input('Enter num ...\n'))
        calc(first, op, second)
        sys.exit(0)    
    
    first = float(sys.argv[1])
    op = sys.argv[2]
    second = float(sys.argv[3])
    calc(first, op, second)
    sys.exit(0)