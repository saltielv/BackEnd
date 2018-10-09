class Dog:
    def __init__(self, name, breed, color, size, weight):
        self.name = name
        self.breed = breed
        self.color = color
        self.size = size
        self.weight = weight
        # print('Hi! My name is:', self.name, 'I\'ve just met you and I love you')
        print(f"Hi! My name is: {self.name}, I have just met you and I love you")
    
    def bark(self, sound = 'whof!'):
        print(self.name + ' says ' + sound)

    def eat(self, type_of_food = 'meat'):
        print(f"{self.name} is eating {type_of_food}, and It's weight is {self.weight}")

    def my_weight(self):
        return f"My name is {self.name} and my weight is {self.weight}"

dog_description = {
    'name': 'Dug',
    'breed': 'Golden retriever',
    'color': 'Brown',
    'size': '58 cm',
    'weight': '30 kg'
}

dog_descriptions = [
    {
    'name': 'Dug',
    'breed': 'Golden retriever',
    'color': 'Brown',
    'size': '58 cm',
    'weight': '30 kg'
    },
    {
    'name': 'Hercules',
    'breed': 'Chihuahua',
    'color': 'Black',
    'size': '45 cm',
    'weight': '15 kg'
    },
    {
    'name': 'Borrego',
    'breed': 'Fresh Poodle',
    'color': 'White',
    'size': '42 cm',
    'weight': '20 kg'
    }
]

# first_dog = Dog('Dug','Cocker','Brown','2','5')
""" first_dog = Dog(**dog_description)
first_dog.bark()
first_dog.eat() """

my_dog_list = []

for description in dog_descriptions:
    new_dog = Dog(**description)
    my_dog_list.append(new_dog)

print(my_dog_list)

for dog in my_dog_list:
    print(dog.my_weight())


# second_dog = Dog