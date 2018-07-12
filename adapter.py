# -*- coding:utf8 -*-
import os


class Dog(object):
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Cat(object):
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow~"


class Human(object):
    def __init__(self):
        self.name = "Human"

    def speak(self):
        return "hello"


class Car(object):
    def __init__(self):
        self.name = "Car"

    def make_noise(self, octane_level):
        return "vroom%s" % ("!" * octane_level)


class Adapter(object):
    """
    adapts an object by replacing methods.
    Usage:
    dog = Dog
    dog = Adapter(dog, dict(make_noise=dog.bark))
    """
    def __init__(self, obj, adapted_methods):
        """
        we set the adapted methods in the object's dict
        :param obj: obj
        :param adapted_methods: obj.method
        """
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """
        all non-adapted calls are passed to the object
        :param attr:
        :return:
        """
        return getattr(self.obj, attr)


def main():
    objects = []
    dog = Dog()
    objects.append(Adapter(dog, dict(make_noise=dog.bark)))
    cat = Cat()
    objects.append(Adapter(cat, dict(make_noise=cat.meow)))
    human = Human()
    objects.append(Adapter(human, dict(make_noise=human.speak)))
    car = Car()
    car_noise = lambda: car.make_noise(3)
    objects.append(Adapter(car, dict(make_noise=car_noise)))

    for obj in objects:
        print("A", obj.name, "gose", obj.make_noise())


if __name__ == '__main__':
    main()
