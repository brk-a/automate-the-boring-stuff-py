#!/usr/bin/env python3

import sys

def login(username, password):
    if username and password:
        print(f'user {username} created successfully')
    res = input('log in now? y/n\t')
    if res == 'y' or res == 'Y': #Yes, YES, yes
        login_username = input('Enter username... ')
        login_password = input('Enter password... ')
    elif res == 'n' or res == 'N': #No, NO, no
        print(f'Thank you, {username}. \nExiting...')
        return
    else:
        print(f'invalid input \nExiting...')
        return

    if username == login_username and password == login_password:
        print(f'logged in as {username}')
    else:
        print('invalid credentials')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        # print('Usage 1: ./3-simple_login.py <username> <password>')
        # print('Usage 2: python3 3-simple_login.py')
        username = input('Enter username... ')
        password = input('Enter password... ')
        login(username, password)
        sys.exit(0)

    username = sys.argv[1]
    password = sys.argv[2]
    login(username, password)
    sys.exit(0)