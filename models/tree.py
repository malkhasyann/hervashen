class Tree:
    def __init__(self, pos=(0,0)):
        self.__pos = pos

    @property
    def pos(self):
        return self.__pos

    def photosynthesis(self):
        return 100

    def __str__(self):
        return f'Tree at {self.__pos}'