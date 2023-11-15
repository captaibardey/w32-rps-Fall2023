import rules
import random 

def getThrowPlayer() -> str:
    print(f"Please type your throw: {', '.join(rules.rules_dict.keys())}")
    input_str = input().lower() 
    while input_str not in rules.rules_dict.keys():
        print(f"Invalid input: please try again with input {', '.join(rules.rules_dict.keys())}")
        input_str = input().lower() 
    return input_str

def getThrowComputer() -> str:
    return random.choice(rules.rules_dict.keys())

getThrowPlayer()