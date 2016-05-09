import betago.dataloader.goboard as B
import danian.coreai as C
import danian.daniancore as D
import random

random.seed()

def fchoice(board, color):
    moves = [(i,j) for i in range(0,9) for j in range(0,9)]
    move = (-1,-1)
    i = 0
    while True:
        if i > 30:
            return None
        move = random.choice(moves)
        if board.is_move_legal(color, move):
            break
        moves.remove(move)
        i += 1
    return move

def schoice(board, num, color):
    moves = [(i,j) for i in range(0,9) for j in range(0,9)]
    #print(board)
    out_list = []
    while True:
        move = random.choice(moves)
        if board.is_move_legal(color, move):
            out_list.append(move)
            if len(out_list) == num:
                break
        moves.remove(move)
    #print(out_list)
    return out_list

def winner(board):
    return 'b'

def main():
    #ai = C.CoreAI(winner, fchoice, schoice, 3, 3)
    d = D.DaNiAn(winner, fchoice, schoice, 3, 3)
    d.run()


if __name__ == '__main__':
    main()


