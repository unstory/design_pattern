# -*- coding:utf8 -*-
import copy

class Prototype:
    def __init__(self):
        self._object = {}

    def register_object(self, name, obj):
        self._object[name] = obj

    def unregister_object(self, name):
        del self._object[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._object.get(name))
        obj.__dict__.update(attr)
        return obj


def main():
    class A:
        def __str__(self):
            return "I am A"

    a = A()
    prototype = Prototype()
    prototype.register_object("a", a)
    b = prototype.clone("a", a=1, b=2, c=3)

    print(a)
    print(b.a, b.b, b.c)

if __name__ == '__main__':
    main()
