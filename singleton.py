# -*- coding:utf8 -*-
import datetime
import time

# 单例
# purpose
# 保证一个类只能有一个示例，并提供一个访问它的全局点
# 适用性
# 当类只能有一个示例而且客户可以从一个众所周知的访问点访问它时


class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance



class SingleSpam(Singleton):
    def __init__(self):
        self.name = "singleton"
        self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(self.time)
        time.sleep(10)


if __name__ == '__main__':
    s1 = SingleSpam()
    s2 = SingleSpam()
    print(id(s1))
    print(id(s2))