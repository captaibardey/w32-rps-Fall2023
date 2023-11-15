def getThrowsRPS():
    print("Please type your throw: 'rock', 'paper', or 'scissors'")
    input_str = input().lower() 
    while input_str not in set(['rock', 'paper', 'scissors']): # TODO get this from the dict keys once that's decided
        print("Invalid input: please try again with input 'rock', 'paper', 'scissors'")
        input_str = input().lower() 
    return input_str

def getThrowsRPSLS():
    print("Please type your throw: 'rock', 'paper', 'scissors', 'lizard', or 'spock'")
    input_str = input().lower() 
    while input_str not in set(['rock', 'paper', 'scissors', 'lizard', 'spock']):  # TODO get this from the dict keys once that's decided
        print("Invalid input: please try again with input 'rock', 'paper', 'scissors', 'lizard', or 'spock' ")
        input_str = input().lower() 
    return input_str
