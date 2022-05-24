
class HotBeverage:
    def __init__(self) -> None:
        self.price = 0.30
        self.name = "hot beverage"

    def description(self) -> str:
        return ("Just some hot water in a cup.")

    def __str__(self) -> str:
        return("name : %s\nprice : %.2f\ndescription : %s\n"%(
            self.name,
            self.price,
            self.description()
        ))

class Coffee(HotBeverage):
    def __init__(self) -> None:
        self.name = "coffee"
        self.price = 0.40

    def description(self) -> str:
        return ("A coffee, to stay aweke.")

class Tea(HotBeverage):
    def __init__(self) -> None:
        self.name = "tea"
        self.price = 0.30

    def description(self) -> str:
        return ("Just some hot water in a cup.")

class Chocolate(HotBeverage):
    def __init__(self) -> None:
        self.name = "chocolate"
        self.price = 0.50

    def description(self) -> str:
        return ("Chocolae, sweet chocolate...")

class Cappuccino(HotBeverage):
    def __init__(self) -> None:
        self.name = "cappuccino"
        self.price = 0.45
    
    def description(self) -> str:
        return ("Un po' di Italia nella sua tazza!")

def test():
    hb = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    capuccino = Cappuccino()
    print(hb)
    print(coffee)
    print(tea)
    print(chocolate)
    print(capuccino)

if __name__ == '__main__':
    try:
        test()
    except Exception as e:
        print(e)