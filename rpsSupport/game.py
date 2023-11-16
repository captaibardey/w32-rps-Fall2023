from . import getThrows
from . import rules

def playeroutcome(gamedict, playerthrow: str, computerthrow: str) -> str:
    win = "win"
    lose = "lose"
    tie = "tie"
    print ("computer choses", computerthrow)
    if playerthrow == computerthrow:
        return tie
    else:
        if computerthrow in gamedict[playerthrow]:
            return win
        else:
            return lose

def playGame():
    playerthrow = getThrows.getThrowPlayer()
    computerthrow = getThrows.getThrowComputer()
    return playeroutcome(rules.rules_dict, playerthrow, computerthrow)
