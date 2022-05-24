#!/usr/bin/python3 

def numbers():
    with open("numbers.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            tmp = line.split(",")
            for it in tmp:
                print(it.strip(" \n"))

if __name__ == '__main__':
    try:
        numbers()
    except Exception as e:
        print(e)
        pass