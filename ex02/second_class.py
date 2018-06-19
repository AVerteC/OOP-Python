from first_class import FirstClass


class SecondClass(FirstClass):

    def __init__(self, name):
        super().greeting(name)


