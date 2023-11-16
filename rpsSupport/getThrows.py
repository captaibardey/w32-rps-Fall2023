from . import rules
import random

def getThrowPlayer() -> str:
    print(f"Please type your throw: one of {', '.join(rules.rules_dict.keys())}")
    input_str = input().lower() 
    while input_str not in list(rules.rules_dict.keys()):
        print(f"Invalid input: please try again with one of {', '.join(rules.rules_dict.keys())}")
        input_str = input().lower() 
    return input_str

def getThrowComputer() -> str:
    return random.choice(list(rules.rules_dict.keys()))
