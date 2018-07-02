# _*_ coding: utf-8 _*_

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