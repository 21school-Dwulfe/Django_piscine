import random
from beverages import HotBeverage, Tea, Coffee, Chocolate, Cappuccino

class CoffeeMachine:
    def __init__(self) -> None:
        self.garanty = 10

    class EmptyCup(HotBeverage):
        def __init__(self) -> None:
            self.name = "empty cup"
            self.price = 0.90
        
        def description(self) -> str:
            return ("An empty cup? Gimme my monye back!")
    
    class BrokenMachineException(Exception):
        def __init__(self) -> None:
            super().__init__("This coffee machine has to be repaired.")
    
    def serve(self, invoice: HotBeverage) -> HotBeverage():
        if self.garanty == 0:
            raise CoffeeMachine.BrokenMachineException()
        self.garanty -= 1
        if random.randint(0, 5) == 0:
            return (CoffeeMachine.EmptyCup())
        return (invoice())
    
    def repair(self) -> None:
        self.garanty = 10
        
def test():
    coffeeMachine = CoffeeMachine()
    i = 0
    while i <= 21:
        try:
            pass
            print(coffeeMachine.serve(
                random.choice([Coffee, Tea, Chocolate, Cappuccino])
            ))
            i += 1
        except Exception as e:
            print(e)
            coffeeMachine.repair()

if __name__ == '__main__':
    test()

