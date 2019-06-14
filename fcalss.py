"""
this file include a class
Author:Richard Chen
Create Date:2019-06-12
Update Date:2019-06-12
"""

'''
define a python class
'''


class User:  # this is a base class

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        info = 'your name is ' + self.name + ', your age is ' + str(self.age)
        print(info)


class VipUser(User):  # VipUser is the subclass of User
    __scores = 0

    def __init__(self, name, age, identity):
        super().__init__(name, age)
        self.identity = identity

    def set_scores(self, scores):
        self.__scores = scores

    def get_scores(self):
        return self.__scores

    def show_info(self):  # override the method of sup-class
        info = 'your name is ' + self.name + ', your age is ' + \
               str(self.age) + ', your id is ' + str(self.identity)
        print(info)
