#!/usr/bin/python3

def var():
    v = 42
    print(v, "has a type", type(v))
    v = "42"
    print(v, "has a type", type(v))
    v = "quarante-deux"
    print(v, "has a type", type(v))
    v = 42.0
    print(v, "has a type", type(v))
    v = True
    print(v, "has a type", type(v))
    v = [42]
    print(v, "has a type", type(v))
    v = {42:42}
    print(v, "has a type", type(v))
    v = (42,)
    print(v,"has a type" ,type(v))
    v = set()
    print(v, "has a type", type(v))

if __name__ == '__main__':
    var()