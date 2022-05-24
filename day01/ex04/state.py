#!/usr/bin/python3
import sys

def get_key_from_value(dict: dict, value):
    for key, item in dict.items():
        if item == value:
            return key
    return None

def read_from_dict(key : str):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    arr = key.split()
    key = " ".join([item.lower().capitalize() for item in arr])
    v = get_key_from_value(capital_cities, key.strip())
    if v:
        return get_key_from_value(states, v)
    return ("Unknown capital city ")

def main():
    if len(sys.argv) == 2:
        print(read_from_dict(sys.argv[1]))

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        pass