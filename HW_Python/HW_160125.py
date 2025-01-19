

class Animals:
    def __init__(self, type, living_environment, predator_or_herbivore, speed_moving):
        self.type = type
        self.living_environment = living_environment
        self.predator_or_herbivore = True
        self.speed_moving = speed_moving
        self._colors = ""
        self.__rare = "Ordinary"
        self.is_awake = False

    def wake_up(self):
        if self.is_awake:
            print(f"{self.type} is already wake up.")
        else:
            print(f"{self.__rare} {self.type} wake up.")
            self.is_awake = True

    def sleep(self):
        if self.is_awake:
            print(f"{self.type} is sleeping.")
        else:
            print(f"{self.type} already sleep. {self.type} must wake up!")
            self.is_awake = False


    def eating(self):
        if self.is_awake:
            print(f"There is {self.type} eat food at {self.living_environment}.")
        else:
            print("It must wake up!")

    def moving(self):
        if self.is_awake:
            print(f"The {self.type} moves at a speed of {self.speed_moving} km per hour.")
        else:
            print("It must wake up!")

    def hunting(self):
        if self.is_awake:
            print(f"The {self.type} is ready for hunting.")
        elif self.predator_or_herbivore:
            print(f"The {self.type} is hunting")
        elif not self.predator_or_herbivore:
            print(f"The {self.type} is herbivore")
        else:
            print("It must wake up!")

    def drinking(self):
        if self.is_awake:
            print(f"The {self.type} is drinking.")
        else:
            print("It must wake up!")

class Dog(Animals):
    def __init__(self, type, living_environment, predator_or_herbivore, speed_moving, name, age, breed):
        super().__init__(type, living_environment, predator_or_herbivore, speed_moving)
        self.name = name
        self.age = age
        self.breed = breed


    def playing(self):
        if self.is_awake:
            print(f"{self.type} {self.breed} {self.name} {self.age} years old is playing.")
        else:
            print(f"{self.name} must wake up!")

    def sleep(self):
        super().sleep()
        print(f"{self.type} {self.name} is sleeping in the {self.living_environment}.")

    @property
    def rare(self):
        return self.__rare

    @rare.setter
    def rare(self):
        self.__rare = "unusual"


dog = Dog(type="Dog", living_environment="house", predator_or_herbivore="predator", speed_moving="25", name="Barabulka", age=2, breed="German shepherd")

dog.eating()
dog.wake_up()
dog.eating()
dog.playing()
dog.hunting()
dog.moving()
dog.sleep()
dog.moving()

dog.sleep()
_dog.__rare()