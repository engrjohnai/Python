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


'''
class Car:
    brand = "X"
    def __init__(self, name, year, color, mileage):
        self.name = name   
        self.year = year    
        self.color = color 
        self.mileage = mileage 

    def __add__(self, other):
        self.mileage = self.mileage + other.mileage

    def drive(self, other):
        return f"New mileage: {self.mileage}"

    def __str__(self):
        return f"Car: {self.name}, {self.year}, {self.color}, {self.mileage}"



