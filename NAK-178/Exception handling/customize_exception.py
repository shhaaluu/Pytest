class CoffeeTooHotException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class CoffeeTooColdException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class CoffeeCup:
    def __init__(self, temperature):
        self.__temperature = temperature

    def drink_coffee(self):
        if self.__temperature > 85:
            raise CoffeeTooHotException('Coffee Temperature:' + str(self.__temperature))
        elif self.__temperature < 65:
            raise CoffeeTooColdException('Coffee Temperature: ' + str(self.__temperature))

        else:
            print('Coffee Ok to Drink')

cup = CoffeeCup(50)
cup.drink_coffee()   
