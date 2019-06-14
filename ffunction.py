"""
this file include some function definition
Author: Richard Chen
Create Date: 2019-06-12
Update Date: 2019-06-12
"""

import json

'''
function: get the formatted full name   
annotation: return the full name, the  default arguments must on the
right of no-default arguments.
'''


def get_formatted_name(first_name, lat_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + lat_name
    else:
        full_name = first_name + ' ' + lat_name
    return full_name.title()


'''
function: copy list 'src' to list 'dst'
annotation: list 'src' and list 'dst' will be changed
'''


def f_copy(src, dst):
    while src:
        temp = src.pop()
        dst.append(temp)


'''
function: get any arguments, and print them
annotation: this function can get one or more arguments, and print all arguments.
'''


def f_get_any_args(size, *args):
    print('the size of args is ' + str(size))
    for arg in args:
        print(arg)


def f_get_any_key_args(first, last, **user_info):
    profile = dict()
    profile['first_name'] = first
    profile['last_name'] = last
    for k, v in user_info.items():
        profile[k] = v
    return profile


'''
when call this function, you must write the 'size=' implicitly,
otherwise, the python interpreter will interpret the value of 
size to any-argument
'''


def f_get_args(*args, size):
    print('the size of args is ' + str(size))
    for arg in args:
        print(arg)


def f_division(left, right):
    try:
        result = left / right
    except ZeroDivisionError:
        print("can't divide by zero")
    else:
        print(result)


'''
function: return the username if 'user.json' exists, or return None
annotation:
'''


def get_user():
    try:
        with open('user.json', 'r') as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username


'''
function: print greet if username isn't null, or write new name
annotation:
'''


def greet_user(username):
    if username:
        print('welcome back, ' + username)
    else:
        print('please input your name: ')
        name = input()
        with open('user.json', 'w') as file:
            json.dump(name, file)


def op_dumps():
    info = {'name': 'richard',
            'sex': 'boy',
            'age': 24}
    with open('info.json', 'w') as fp:
        s_info = json.dumps(info)
        fp.write(s_info)


def op_loads():
    with open('info.json', 'r') as fp:
        content = fp.read()
        d_info = json.loads(content)
        print(type(content))
        print(type(d_info))
