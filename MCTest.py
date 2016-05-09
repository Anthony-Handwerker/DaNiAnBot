import betago.dataloader.goboard as B
import danian.coreai as C
import danian.daniancore as D
import testfunctions as T
import random



def main():
    #ai = C.CoreAI(winner, fchoice, schoice, 3, 3)
    d = D.DaNiAn(T.TestFunctions.naive_winner, T.TestFunctions.random_fchoice, T.TestFunctions.random_schoice, 3, 3)
    d.run()


if __name__ == '__main__':
    main()


