from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    def move(self):
        return "Moving"

class Dog(Animal):
    @property
    def make_sound(self):
        return "Bark"
    

class Cat(Animal):
    @property
    def make_sound(self):
        return "Meoww"
    
dog=Dog()




