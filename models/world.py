import time
import random
import os
from models.sun import Sun
from models.oxygen import Oxygen
from models.grass import Grass
from models.frog import Frog
from models.tree import Tree


class World:
    def __init__(
        self, 
        sun=Sun(is_shining=True), 
        oxygen=Oxygen(), 
        grass=Grass(), 
        animals=[Frog('Chunchurik', True, True, [5,5])], 
        trees=[Tree([1,1])], 
        clock=8
    ):
        self.sun = sun
        self.oxygen = oxygen
        self.grass = grass
        self.__animals = animals
        self.__trees = trees
        self.__clock = clock

    # @property
    # def clock(self):
    #     return self.__clock

    # @clock.setter
    # def clock(self, value:int):
    #     self.__clock = value

    def add_animal(self, animal):
        self.__animals.append(animal)

    def add_tree(self, tree):
        self.__trees.append(tree)

    def __is_day(self):
        if 7 <= self.__clock <=18:
            return True
        return False

    def __trees_work(self):
        for tree in self.__trees:
            self.oxygen.volume += tree.photosynthesis()

    def __animals_move(self):
        for animal in self.__animals:
            if random.randint(-1, 1):
                animal.move()

    def __animals_eat(self):
        for animal in self.__animals:
            if random.randint(0, 1):
                animal.eat(self.grass)

    def __animals_breathe(self):
        for animal in self.__animals:
            self.oxygen.being_breathed(animal)

    def __animals_sleep(self):
        for animal in self.__animals:
            if animal.is_awake:
                animal.sleep()

    def __animals_wake_up(self):
        for animal in self.__animals:
            if not animal.is_awake:
                animal.wake_up()

    def __animals_get_hungry(self):
        for animal in self.__animals:
            animal.get_hungry()

    def __info_animals(self):
        return "Animals:\n" + '\n'.join(['\t' + str(x) for x in self.__animals]) + '\n'

    def __info_trees(self):
        return "Trees:\n" + '\n'.join(['\t' + str(x) for x in self.__trees]) + '\n'

    def __collect_dead_animals(self):
        alive = []
        for animal in self.__animals:
            if animal.is_dead:
                animal.dead_message()
                continue
            alive.append(animal)
        self.__animals = alive

    def __str__(self):
        message = f"It is {self.__clock}\n"
        message += str(self.sun) + '\n'
        message += str(self.oxygen) + '\n'
        message += self.__info_animals()
        message += self.__info_trees()
        return message

    def run(self):
        while True:
            os.system('clear')
            print(self)
            if self.__is_day():
                self.sun.is_shining = True
                self.__trees_work()
                self.__animals_wake_up()
                self.__animals_move()
                self.__animals_eat()
                self.__animals_breathe()
            else:
                self.sun.is_shining = False
                self.__animals_sleep()
            self.__animals_get_hungry()
            self.__collect_dead_animals()
            time.sleep(1.5)
            self.__clock = (self.__clock + 1) % 24