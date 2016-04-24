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

    def kills(self, tri):
        out = set()
        rev_dict = {'B':'W','W':'B'}
        color = rev_dict.get(tri[0])
        for dir in [(0,1),(1,0),(0,-1),(-1,0)]:
            new_tri = (color, tri[1] + dir[0], tri[2] + dir[1])
            if self.valid(new_tri):
                out = out.union(self.kill_helper(new_tri))
        return out

    def kill_helper(self, tri):
        if self.board[tri[1]][tri[2]] != tri[0]:
            return set()
        g = self.get_group(tri)
        surr = self.get_surrounding(g)
        rev_dict = {'B':'W','W':'B'}
        color = rev_dict.get(tri[0])
        if(self.is_killed(color, surr)):
            return g
        else:
            return set()

    def get_group(self, move_tri):
        searching = set()
        to_search = set()
        searched = set()
        searching.add((move_tri[1],move_tri[2]))
        while True:
            changes = 0
            for k in searching:
                for j in [(0,1),(1,0),(0,-1),(-1,0)]:
                    newmove = (k[0] + j[0], k[1] + j[1])
                    if self.valid((move_tri[0], newmove[0], newmove[1])) and newmove not in searching \
                            and newmove not in searched and newmove not in to_search:
                        if self.board[newmove[0]][newmove[1]] == move_tri[0]:
                            to_search.add((newmove[0], newmove[1]))
                            changes += 1
                searched.add(k)
            searching = to_search.copy()
            to_search.clear()
            if len(searching) == 0:
                break
        return searched

    def get_surrounding(self, g): # returns what spaces if filled will kill group g
        group = set()
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                if (i,j) not in g:
                    if not set([(i+1,j),(i-1,j),(i,j+1),(i,j-1)]).isdisjoint(g):
                        group.add((i,j))
        return group

    def is_killed(self, color, surr):
        for pos in surr:
            if self.board[pos[0]][pos[1]] != color:
                return False
        return True


    def are_adjacent(self, move1, move2):
        return abs(move1[0]-move2[0]) <= 1 and abs(move1[1]-move2[1]) <= 1 and move1 != move2

    def valid(self, move_tri):
        return move_tri[1] >= 0 and move_tri[2] >= 0 and move_tri[1] < len(self.board) and \
               move_tri[2] < len(self.board)

    def illegal(self, move_tri):
        return False

    def ko(self, move_tri):
        return False

    def play_move(self, move_tri):
        self.board[move_tri[1]][move_tri[2]] = move_tri[0]
        g = self.kills(move_tri)
        self.rem(g)

    def rem(self, g):
        for move in g:
            self.board[move[0]][move[1]] = ''

    def load_from_sgf(self, sgf):
        mlist = parse_sgf_into_move_list(sgf)
        for move in mlist:
            mtri = parse_move_into_tri(move)
            self.board[mtri[1]][mtri[2]] = mtri[0]

    def print_board(self):
        d = {'':'.','B':'X','W':'O'}
        for i in self.board:
            line = ""
            for j in i:
                line += d.get(j)
            print(line)





