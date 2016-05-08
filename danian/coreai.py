
class CoreAI:
    def __init__(self, winner = None, fdecision = None, sdecision = None, breadth = 5, depth = 3): #arbitrary breadth/depth choices
        self.winner = winner # should accept a board and return n
        self.fast_decision = fdecision # should accept a board, return a move.
        slef.slow_decision = sdecision # should accept a number n and a board, and return n moves in a list.
        self.root = MCTreeNode()
        self.breadth = breadth
        self.depth = depth

    def get_move(self, board): # skeleton functions are best functions
        self.expansion(board)
        return self.decision(board)

    def expansion(self, board):
        self.root = MCTreeNode()
        self.expansion_helper(self.root, board, self.depth)
        winrate_max = 0.0
        best_move = ''
        for node in self.root.children:
            winrate = node.wins[0] / (node.wins[0] + node.wins[1])
            if winrate > winrate_max:
                winrate_max = winrate
                best_move = node.move
        return best_move



    def expansion_helper(self, node, board, level):
        if level == 0:
            while True:
                move = fast_decision(board)
                if move == '':
                    break
                board.play_move(move)
            winner = winner(board)
            if winner == 'B':
                node.wins = [1, 0]
            else:
                node.wins = [0,1]
            node.back_propagate()
            return

        moves = self.slow_decision(breadth, board)
        for i in moves:
            new_board = board.project(i) # need to write this function, make a new board based on a move
            child = MCTreeNode()
            child.move = i
            node.add_child(child)
            self.expansion_helper(child, new_board, level-1)




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