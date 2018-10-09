class Robot:
    #message = 'Hello'
    def __init__(self, message = 'Hello'):
        self.message = message
    def say_hello(self, text = ''):
        print(self.message, text)


class Robot_v2(Robot):
    def walk(self):
        print('I can walk!')

my_first_robot = Robot()
my_second_robot = Robot()
my_third_robot = Robot_v2()

my_first_robot.message = 'Hola'

my_first_robot.say_hello()
my_second_robot.say_hello()
my_third_robot.say_hello('Everybody I\'m version two')



