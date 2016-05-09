import random

random.seed()


class BotFunctions:
    @staticmethod
    def random_fchoice(board, color):
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

    @staticmethod
    def random_schoice(board, num, color):
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

    @staticmethod
    def b_winner(board):
        return 'b'

    @staticmethod
    def naive_winner(board):
        score = BotFunctions.get_bias(board, 5.5)
        spaces = [(i,j) for i in range(0,9) for j in range(0,9)]
        for i in range(0,9):
            for j in range(0,9):
                point = (i,j)
                subscore, color = BotFunctions.explore(board, point, spaces)
                if color == 'w':
                    score += subscore
                elif color == 'b':
                    score -= subscore
        if score > 0:
            return 'w'
        else:
            return 'b'

    @staticmethod
    def explore(board, point, spaces):
        if point in board.board:
            return (0, board.board[point])
        if point not in spaces:
            return (0, '')
        direcs = [(0,-1), (-1,0), (0,1), (1,0)]
        spaces.remove(point)
        score = 1
        color = ''
        for d in direcs:
            new_point = (point[0] + d[0], point[1] + d[1])
            s, c = BotFunctions.explore(board, new_point, spaces)
            if c == 'F':
                return (0, 'F')
            elif color == '':
                color = c
            elif color != c and c != '':
                return (0, 'F')
            score += s
        return (score, color)






    @staticmethod
    def get_bias(board, komi): # returned in extra points for white
        bias = komi
        for letter in board.board.values():
            if letter == 'b':
                bias -= 1
            else:
                bias += 1
        return bias