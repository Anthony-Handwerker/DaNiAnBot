import betago.dataloader.goboard as B
import danian.coreai as C
import danian.daniancore as D
import danian.botfunctions as F
import random

# main run. Add functions to  danian/botfunctions.py, call them in the D.DaNiAn call.

def main():
    #ai = C.CoreAI(winner, fchoice, schoice, 3, 3)
    d = D.DaNiAn(F.BotFunctions.naive_winner, F.BotFunctions.random_fchoice, F.BotFunctions.random_schoice, 30, 1)
    d.run()


if __name__ == '__main__':
    main()

