import random

def getThrowPlayer(rules_dict : dict[str, list[str]]) -> str:
    print(f"Please type your throw: one of {', '.join(rules_dict.keys())}")
    input_str = input().lower() 
    while input_str not in list(rules_dict.keys()):
        print(f"Invalid input: please try again with one of {', '.join(rules_dict.keys())}")
        input_str = input().lower() 
    return input_str

def getThrowComputer(rules_dict : dict[str, list[str]]) -> str:
    return random.choice(list(rules_dict.keys()))
