
class Intern:

    class Coffee:
        def __str__(self) -> str:
            return ("This is the worst coffee you ever tasted.")

    def  __init__(self, name=None) -> None:
        self.name = "My name? I'm nobody, an intern, I have no name." if name==None else name

    #   For printing object
    def __str__(self) -> str:
        return self.name

    def work(self) -> None:
        raise Exception("I'm just an intern, I cant't do that...")
    
    def make_coffee(self) -> Coffee():
        return (Intern.Coffee())

def test():
    print("____Test____")
    no = Intern()
    mark = Intern('Mark')
    print(no)
    mark.work()
   
   
def test_coffee():
    print("____Test Coffee_____")
    no = Intern("Mark")
    coffee = no.make_coffee()
    print(f"{coffee}")

if __name__ == '__main__':
    try:
        test()
    except Exception as e:
        print(e)
    try:
        test_coffee()
    except Exception as e:
        print(e)






