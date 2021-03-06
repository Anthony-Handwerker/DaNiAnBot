
import copy

color_switch = {'b':0, 'w':1}
PASS_TYPE = None

class CoreAI:
    def __init__(self, winner = None, brain = None, breadth = 3, depth = 5): #arbitrary breadth/depth choices
        self.winner = winner # should accept a board and return n
        self.brain = brain
        self.root = MCTreeNode()
        self.breadth = breadth
        self.depth = depth

    def get_move(self, board, color): # skeleton functions are best functions
        return self.expansion(board, color)

    def expansion(self, board, color):
        self.root = MCTreeNode()
        self.expansion_helper(self.root, board, self.depth, color)
        winrate_max = -1.0
        best_move = None
        for node in self.root.children:
            winrate = node.wins[color_switch[color]] / (node.wins[0] + node.wins[1])
            if winrate > winrate_max:
                winrate_max = winrate
                best_move = node.move
        return best_move

    def expansion_helper(self, node, board, level, color):
        if level == 0:
            while True:
                move = self.brain.top_move(board, color)
                if move is None:
                    break
                board.apply_move(color, (move[0], move[1]))
            # winner = winner(board)
            # if winner == 'B':
            #     node.wins = [1, 0]
            # else:
            #     node.wins = [0, 1]
            node.wins[color_switch[self.winner(board)]] += 1 # temporary scoring code
            node.back_propagate()
            return

        moves = self.brain.top_moves(board, self.breadth, color)
        for i in moves:
            #print("LEVEL: " + str(level))
            child = MCTreeNode()
            child.move = i
            node.add_child(child)
            if i is None:
                child.wins[color_switch[self.winner(board)]] += 1
                child.back_propagate()
                return
            new_board = copy.deepcopy(board)
            new_board.apply_move(color, (i[0], i[1]))
            
            self.expansion_helper(child, new_board, level-1, board.other_color(color))




class MCTreeNode:
    def __init__(self):
        self.parent = None
        self.children = []
        self.move = ''
        self.wins = [0, 0]
        self.player = 0

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def back_propagate(self):
        if self.parent is not None:
            self.parent.back_propagate_helper(self.wins)

    def back_propagate_helper(self, wins):
        self.wins[0] += wins[0]
        self.wins[1] += wins[1]
        if self.parent is not None:
            self.parent.back_propagate_helper(wins)