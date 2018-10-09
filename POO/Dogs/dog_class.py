class Dog:
    def __init__(self, name, breed, color, size, weight):
        self.name = name
        self.breed = breed
        self.color = color
        self.size = size
        self.weight = weight
        print(f"Hi! My name is: {self.name}, I have just met you and I love you.")
    
    def bark(self, sound = 'whof!'):
        print(f"{self.name} says: {sound}")

    def eat(self, type_of_food = 'meat'):
        print(f"{self.name} is eating {type_of_food}, and It's weight is {self.weight}")

    def my_weight(self):
        return f"My name is {self.name} and my weight is {self.weight}"