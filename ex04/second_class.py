import random
from first_class import FirstClass


class SecondClass(FirstClass):

    def roll_dice():
        print("Method roll_dice in SecondClass called")
        return random.randrange(1,6,1)

    def __init__(self, name):
        num = SecondClass.roll_dice()
        super().hello(name, num)





