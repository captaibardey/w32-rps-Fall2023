import getThrows
import rules

def playeroutcome(gamedict, playerthrow: str, computerthrow: str) -> str:
    print ("computer choses", computerthrow)
    if playerthrow == computerthrow:
        print("tie")
    else:
        if computerthrow in gamedict[playerthrow]:
            print("you win")
        else:
            print("you lose")

def playGame():
    playerthrow = getThrows.getThrowPlayer()
    computerthrow = getThrows.getThrowComputer()
    return playeroutcome(rules.rules_dict, playerthrow, computerthrow)

playGame()
