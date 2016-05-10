__author__ = 'handwa'

from danian import ogsession, coreai
import betago.gosgf.sgf as SGF
import betago.dataloader.goboard as B

class DaNiAn:
    def __init__(self, winner, brain, breadth = 3, width = 3):
        self.og = ogsession.OGSession()
        self.pid = self.og.get_player_id()
        self.games = {}
        self.ai = coreai.CoreAI(winner, brain, breadth, width)
        

    def run(self):
        while True:
            self.accept_challenges()
            self.make_moves()

    def refresh_board(self, gid):
        s = SGF.Sgf_game.from_string(str.encode(self.og.get_sgf(gid)))
        self.games[gid] = (self.games[gid][0], B.GoBoard(9))
        board = self.games[gid][1]
        for item in s.main_sequence_iter():
            color, move = item.get_move()
            if color is not None and move is not None:
                board.apply_move(color, move)

    def accept_challenges(self):
        challenges = self.og.list_challenge_ids()
        for c_id in challenges:
            if(self.og.get_challenge_validity(c_id)):
                body_dict = self.og.accept_challenge(c_id)
                self.game_prep(body_dict['game'])
                print("Accepted challenge " + str(c_id) + " for a game named " + body_dict['name'])
            else:
                self.og.delete_challenge(c_id)
                print("Deleted challenge " + str(c_id))

    def game_prep(self, game_id):
        game_data = self.og.get_game_detail(game_id)
        color = ''
        if game_data['players']['white']['id'] == self.pid:
            color = 'w'
        else:
            color = 'b'
        self.games[game_id] = (color, B.GoBoard(9))

    def check_turn(self, game_id):
        game_data = self.og.get_game_detail(game_id)
        return game_data['gamedata']['clock']['current_player'] == self.pid


    def make_moves(self):
        for game in self.games.keys():
            if self.check_turn(game):
                self.refresh_board(game)
                move = self.ai.get_move(self.games[game][1], self.games[game][0])
                if move is None:
                    self.og.make_move(game, "")
                    games.remove(game)
                #print("Making move " + str(move) + " in game " + str(game))
                #print(self.games[game][1])
                self.og.make_move(game, "abcdefghi"[move[1]] + "abcdefghi"[8-move[0]])
                print("Made move " + str(move) + " in game " + str(game))



