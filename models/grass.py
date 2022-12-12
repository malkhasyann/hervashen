class Grass:
    def __init__(self, point=3):
        self.__point = point

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, value):
        self.__point = value