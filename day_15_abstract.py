# Abstract or Interface
# Force other class to implement certain methods
# Autocomplete
from abc import ABC, abstractmethod


# Abstract class / Interface
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Woof Woof")

    def move(self):
        print("Runnning... 🐕")

    def jump(self):
        print("Jumps 🦘")


class Bird(Animal):
    def make_sound(self):
        print("KOOk KOOK")

    def move(self):
        print("walks..")

    def fly(self):
        print("Flatters..")


maxy = Dog()
maxy.move()

keech = Bird()
keech.fly()
