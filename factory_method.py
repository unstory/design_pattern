# _*_ coding: utf-8 _*_
import random

# 创造型设计模式:
# 提供实例化的方法，为适合的状况提供相应的对象创建方法。
# factory method
# purpose
# 定义一个用于创建对象的接口，让子类决定实例化哪一个类；
# Factory Method 使一个类的实例化延迟到其子类。
# 适用性:
# 当一个类不知道它所必须创建的对象的类的时候
# 当一个类希望由它的子类来指定它所创建的对象的时候


class PetShop:
    def __init__(self, animal_factory=None):
        """
        pet_factory is our abstract factory. We can set it at will
        :param animal_factory:
        """
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print("This is a lovely", pet)
        print("It says", pet.speak())
        print("It eats", self.pet_factory.get_food())


class Dog:
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat:
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


class DogFactory:
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"


class CatFactory:
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"


def get_factory():
    return random.choice([DogFactory, CatFactory])()


if __name__ == '__main__':
    shop = PetShop()
    for i in range(3):
        shop.pet_factory = get_factory()
        shop.show_pet()
        print("=" * 20)

