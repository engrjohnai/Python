class Dog:
    species = "Canis Familiaris"
    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size

    def description(self):
        return f"{self.name} is {self.age} years old that is {self.size} lbs in weight"

    def speak(self, sound):
        self.sound = sound
        return f"{self.name} says {self.sound}"


