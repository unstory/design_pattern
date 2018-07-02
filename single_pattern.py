# -*- coding:utf8 -*-


# 1. 使用模块创建单例
# single_pattern.py
class My_Singleon(object):
    def foo(self):
        pass

my_singleton = My_Singleon()

# main.py
# from single_pattern import My_Singleon


# 2. 使用__new__
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class MyClass(Singleton):
    pass

one_cls = MyClass()
two_cls = MyClass()
print(one_cls is two_cls)
print(id(one_cls), id(two_cls))