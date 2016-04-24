__author__ = 'handwa'

def parse_sgf_into_move_list(sgf):
    sgf_list = sgf.split("\n")
    move_list = [x for x in sgf_list if x[0] == ';']
    return move_list

def parse_move_into_tri(move):
    pos1 = "abcdefghi".find(move[3])
    pos2 = "abcdefghi".find(move[4])
    return (move[1], pos1, pos2)

class GoGame:
    board = []
    color = ''
    def __init__(self, c):
        self.color = c
        for i in range(0, 9):
            self.board.append([])
            for j in range(0, 9):
                self.board[i].append('')

    def load_from_sgf(self, sgf):
        mlist = parse_sgf_into_move_list(sgf)
        for move in mlist:
            mtri = parse_move_into_tri(move)
            self.board[mtri[1]][mtri[2]] = mtri[0]



