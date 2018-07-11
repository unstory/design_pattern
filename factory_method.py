# _*_ coding: utf-8 _*_

# 创造型设计模式:
# 提供实例化的方法，为适合的状况提供相应的对象创建方法。
# factory method
# purpose
# 定义一个用于创建对象的接口，让子类决定实例化哪一个类；
# Factory Method 使一个类的实例化延迟到其子类。
# 适用性:
# 当一个类不知道它所必须创建的对象的类的时候
# 当一个类希望由它的子类来指定它所创建的对象的时候

class ChinaGetter:
    def __init__(self):
        self.trans = dict(dog="小狗", cat="小猫")

    def get(self, msgid):
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)

class EnglishGetter:
    def get(self, msgid):
        return str(msgid)

def get_localizer(language="English"):
    languages = dict(English=EnglishGetter, China=ChinaGetter)
    return languages[language]()


if __name__ == '__main__':
    e, g = get_localizer(), get_localizer("China")
    for msgid in "dog cat parrot bear".split():
        print(g.get(msgid))