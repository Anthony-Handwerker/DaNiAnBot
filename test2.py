__author__ = 'handwa'
from danian import ogsession, gogame
import time

def parseSgfIntoMoveList(sgf):
    sgf_list = sgf.split("\n")
    move_list = [x for x in sgf_list if x[0] == ';']
    return move_list

def main():
    session = ogsession.OGSession()
    print(session.session_key)
    # f = open("games.txt",'r')
    # for line in f:
    #     print(line[:-1])
    # return
    print(session.get_player_id())
    return
    thing = session.get_games()
    print(thing)
    return
    cids = session.list_challenge_ids()
    print(cids)
    game = cids[0]
    print(game)
    g = session.accept_challenge(game)
    session.make_move(g['game'], "ee")
    sgf = session.get_sgf(g['game'])
    mlist = parseSgfIntoMoveList(sgf)
    while True:
        print("Sleeping...")
        time.sleep(1)
        sgf = session.get_sgf(g['game'])
        newlist = parseSgfIntoMoveList(sgf)
        if(mlist != newlist):
            break
    session.make_move(g['game'], "aa")
    sgf = session.get_sgf(g['game'])
    gg = gogame.GoGame('B')
    gg.load_from_sgf(sgf)
    print(gg.board)
    mlist = parseSgfIntoMoveList(sgf)
    print(mlist)

    print()

if __name__=='__main__':
    main()
