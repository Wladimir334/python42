

class Animals:
    def __init__(self, type, living_environment, size, speed_moving):
        self.type = type
        self.living_environment = living_environment
        self.size = size
        self.speed_moving = speed_moving
        self._colors = ""
        self.__rare = "Ordinary"

    def sleep(self):
        if