# -*- coding: utf-8 -*-
# @FileName: zoo.py
# @Time    : 2021/1/2 8:12 下午
# @Author  : zhan
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def __init__(self, kind, shape, character):
        self.kind = kind
        self.shape = shape
        self.character = character

    @property
    def is_ferocious(self):
        if self.shape == '中' and self.character == '凶猛':
            return 1
        else:
            return 0


class Cat(Animal):
    voice = 'miao'

    def __init__(self, name, kind, shape, character):
        super().__init__(kind, shape, character)
        self.name = name

    @property
    def is_pet(self):
        if self.is_ferocious:
            return 0
        else:
            return 1


class Dog(Animal):
    voice = 'wang'

    def __init__(self, name, kind, shape, character):
        super().__init__(kind, shape, character)
        self.name = name

    @property
    def is_pet(self):
        if self.is_ferocious:
            return 0
        else:
            return 1


class Zoo(object):
    def __init__(self, name):
        self.name = name

    def add_animal(self, animal):
        """
        添加动物
        :param animal:
        :return:
        """
        item = type(animal).__name__
        if item not in self.__dict__:
            self.__dict__[item] = item
        else:
            print(f'{item}已经存在')


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    print(f'是否凶猛：{cat1.is_ferocious}, 宠物：{cat1.is_pet}')

    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 重复添加
    z.add_animal(cat1)

    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    have_dog = hasattr(z, 'Dog')
    print(have_cat, have_dog)
