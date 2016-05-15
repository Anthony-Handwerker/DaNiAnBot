#!/usr/bin/env Python3
import betago.dataloader.goboard as B
import danian.coreai as C
import danian.daniancore as D
import danian.botfunctions as F
from danian.neural_network import NeuralNetwork
import random

# main run. Add functions to  danian/botfunctions.py, call them in the D.DaNiAn call.

def main():
    #ai = C.CoreAI(winner, fchoice, schoice, 3, 3)
    d = D.DaNiAn(F.BotFunctions.naive_winner, NeuralNetwork('brain') , 3, 3)
    d.run()


if __name__ == '__main__':
    main()


