#!/usr/bin/python3

import sys

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
    key = " ".join([item.lower().capitalize() for item in arr]).strip()
    if  key in states:
        result = capital_cities[states[key]]
        return result
    else:
        return ("Unknown state")

def main():
    if len(sys.argv) == 2:
        print(read_from_dict(sys.argv[1]))

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        pass