import getThrows
import rules

def playeroutcome(gamedict, playerthrow: str, computerthrow: str) -> str:
    if playerthrow == computerthrow:
        return "tie"
    if computerthrow in gamedict[playerthrow]:
        return "win"
    else:
        return "lose"

def playGame():
    playerthrow = getThrows.getThrowPlayer()
    computerthrow = getThrows.getThrowComputer()
    return playeroutcome(rules.rules_dict, playerthrow, computerthrow)
