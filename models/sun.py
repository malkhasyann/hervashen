class Sun:
    def __init__(self, is_shining:bool):
        self.__is_shining = is_shining

    @property
    def is_shining(self):
        return self.__is_shining
    
    @is_shining.setter
    def is_shining(self, value:bool):
        self.__is_shining = value

    def __str__(self):
        return f'The sun is {"shining" if self.is_shining else "not shining"}.'