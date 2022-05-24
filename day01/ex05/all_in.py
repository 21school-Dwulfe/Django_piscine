import sys

def get_key_from_value(dict: dict, value:str):
    for key, item in dict.items():
        if item.upper() == value.upper():
            return key
    return None

def get_value_from_key(dict: dict, value:str):
    for key, item in dict.items():
        if key.upper() == value.upper():
            return item
    return None

def check_dict(input:str):
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
    state_item =  get_value_from_key(states, input)
    capital_item = get_key_from_value(capital_cities, input)
    if state_item:
        print(input, "is a state of", capital_cities[state_item])
    elif capital_item:
        print(input, "is the capital of", get_key_from_value(states, capital_item))
    else:
        print(input, "is neither a capital city nor a state")


def main():
    if len(sys.argv) == 2:
        arr = sys.argv[1].split(",")
        for item in arr:
            tmp = item.strip()
            if tmp == "":
                continue
            check_dict(tmp)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        with sys.stderr as cerr:
            print(e, file=cerr)
        pass