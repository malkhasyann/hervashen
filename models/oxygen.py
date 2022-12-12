class Oxygen:
    def __init__(self, volume:int=1000):
        self.__volume = volume
    
    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value:int):
        if value < 0:
            raise Exception('Can\'t set negative volume for oxygen')
        self.__volume = value

    def being_breathed(self, animal):
        self.volume -= animal.lung

    def __str__(self):
        return f'Volume of oxygen in air: {self.__volume}'

    