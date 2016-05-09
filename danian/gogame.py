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
    past_states = []
    def __init__(self, c):
        self.color = c
        for i in range(0, 9):
            self.board.append([])
            for j in range(0, 9):
                self.board[i].append('')

    def kills(self, tri):
        out = set()
        color = 'B' if tri[0] == 'W' else 'W'
        for dir in [(0,1),(1,0),(0,-1),(-1,0)]:
            new_tri = (color, tri[1] + dir[0], tri[2] + dir[1])
            if self.valid(new_tri):
                out = out.union(self.kill_helper(new_tri))
        return out
    
    def compact_state(self):
        flat_board = [item for column in board for item in column];
        num_positions = len(flat_board)
        #TODO: Make sure number can handle what we're storing in it.
        result = 0
        for i in range(0, num_positions):
            pos_state = 0
            if flat_board[i] == 'B':
                pos_state = 1
            elif flat_board[i] == 'W':
                pos_state = 2
            result |= 2^(2 * i) * pos_state
        return result
    
    def kill_helper(self, tri):
        if self.board[tri[1]][tri[2]] != tri[0]:
            return set()
        g = self.get_group(tri)
        surr = self.get_surrounding(g)
        color = 'B' if tri[0] == 'W' else 'W'
        if(self.is_killed(color, surr)):
            return g
        else:
            return set()

    def get_group(self, pos):
        searching = set()
        to_search = set()
        searched = set()
        searching.add((pos[0],pos[1]))
        color = self.board[pos[0], pos[1]]
        while True:
            changes = 0
            for k in searching:
                for j in [(0,1),(1,0),(0,-1),(-1,0)]:
                    newmove = (k[0] + j[0], k[1] + j[1])
                    if self.valid(newmove[0], newmove[1]) and newmove not in searching \
                            and newmove not in searched and newmove not in to_search:
                        if self.board[newmove[0]][newmove[1]] == color:
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

    def is_killed(self, pos):
        surrounding = self.get_surrounding(self.get_group(pos))
        color = 'B' if self.board[pos[0], pos[1]] == 'W' else 'W'
        for pos in surr:
            if self.board[pos[0]][pos[1]] != color:
                return False
        return True


    def are_adjacent(self, move1, move2):
        return abs(move1[0]-move2[0]) <= 1 and abs(move1[1]-move2[1]) <= 1 and move1 != move2

    def valid(self, pos):
        return pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(self.board) and \
               pos[1] < len(self.board)

    def illegal(self, color, pos):
        if board[pos[0], pos[1]] != '':
            return True
        if len(kills((color, pos[0], pos[1]))) == 0: # TODO: Refactor kills to use pos
            board[pos[0], pos[1]] = color
            if self.is_killed(pos):
                board[pos[0], pos[1]] = ''
                return True
            board[pos[0], pos[1]] = ''
        if self.ko(color, pos):
            return True
        return False

    def ko(self, color, pos):
        old_pos = self.board[pos[0]][pos[1]]
        self.board[pos[0]][pos[1]] = color
        new_state = self.compact_state()
        self.board[pos[0]][pos[1]] = old_pos
        if new_state in self.past_states:
            return True
        return False

    def play_move(self, color, pos):
        if self.illegal(color, pos):
            return False
        self.board[pos[0]][pos[1]] = color
        g = self.kills(move_tri) # TODO: Refactor kills to use pos
        self.rem(g)
        self.past_states.append(self.compact_state())
        return True

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





