import random
from first_class import FirstClass


class SecondClass(FirstClass):

    def roll_dice(self):
        print("Method roll_dice in SecondClass called")
        return random.randrange(1,6,1)

    def get_hobby(self):
        return self.__dict__["hobby"]

    def __init__(self, name, thishobby):
        self.hobby = thishobby
        num = SecondClass.roll_dice(self)
        super().hello(name, num)



