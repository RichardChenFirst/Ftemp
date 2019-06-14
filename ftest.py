"""
This file is just for test.
Author: Richard Chen
Create Date: 2019-06-06
Update Date: 2019-06-12
"""
import ffunction as ff
import futils as fu
from fcalss import *

'''test code'''
'''
name = get_formatted_name('Richard', 'Chen')
print(name)
name = get_formatted_name('Richard', lat_name='Chen')
print(name)
name = get_formatted_name(first_name='Richard', lat_name='Chen')
print(name)
name = get_formatted_name(lat_name='Chen', first_name='Richard')
print(name)
name = get_formatted_name('richard', 'chen', 'f')
print(name)
'''
fruits = ['apple', 'banana', 'orange', 'grape']
fruits2 = []
ff.f_copy(fruits[:], fruits2)  # fruits[:] is the copy of fruits
fruits2.reverse()
print(fruits)  # fruits don't be changed
print(fruits2)
# ff.f_get_any_args(3, 'richard', 'k', 'chen')
user_profile = ff.f_get_any_key_args('albert', 'einstein',
                                     location='princeton', field='physics')
print(user_profile)
fu.print_greet()

user = User('Richard', 24)
user.show_info()

vip_user = VipUser('Richard', 24, 1)
vip_user.show_info()
vip_user.set_scores(30)
print(vip_user.get_scores())

'''
you must write 'size=3', not '3'
'''
# ff.f_get_args('richard', 'k', 'chen', size=3)

# with open('pi.txt') as file_object:
#     contents = file_object.read()
#     if '3456' in contents:
#         print('the value in pi')
#     else:
#         print('the value not in pi')
# with open('temp.txt', 'a') as temp:
#     temp.write('This is the first line\n')
#     temp.write('This is the second line\n')

# ff.f_division(2, 0)
# file = open('temp.txt', 'r')
# contents = file.read()
# con_list = contents.split()
# print(len(con_list))

number = [1, 3, 5, 7, 9]
# with open('number.json', 'w') as file:
#     json.dump(number, file)
# with open('number.json', 'r') as file:
#     number = json.load(file)
#     print(number)

# username = ff.get_user()
# ff.greet_user(username)

ff.op_dumps()
ff.op_loads()
