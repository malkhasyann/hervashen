import random

class Frog:
    def __init__(
        self, name:str, is_awake:bool, 
        is_breathing:bool, position=[0, 0], stomach=40, lung=5
    ):
        self.name = name
        self.__is_awake = is_awake
        self.__is_breathing = is_breathing
        self.__stomach = stomach
        self.__pos = position
        self.__lung = lung

    @property
    def lung(self):
        return self.__lung
    
    @property
    def is_dead(self):
        return self.__stomach <= 0

    def dead_message(self):
        print(f'{type(self).__name__} {self.name} is dead.')

    @property
    def is_awake(self):
        return self.__is_awake

    @is_awake.setter
    def is_awake(self, value:bool):
        self.__is_awake = value

    @property
    def is_breathing(self):
        return self.__is_breathing

    @is_breathing.setter
    def is_breathing(self, value:bool):
        self.__is_breathing = value

    def move(self):
        self.__pos[0] += random.randint(-1, 1) 
        self.__pos[1] += random.randint(-1, 1) 

    def eat(self, food):
        print(f'{type(self).__name__} {self.name} is eating {type(food).__name__}')
        self.__stomach += food.point

    def get_hungry(self):
        self.__stomach -= 1
    
    def sleep(self):
        self.is_awake = False
        self.is_breathing = False

    def wake_up(self):
        self.is_awake = True
        self.is_breathing = True

    def __str__(self):
        return f'{type(self).__name__} {self.name} at {self.__pos}'\
            f' is {"awake" if self.__is_awake else "sleeping"}'\
            f' and is {"" if self.is_breathing else "not"} breathing: '\
            f' Stomach {self.__stomach} points.'