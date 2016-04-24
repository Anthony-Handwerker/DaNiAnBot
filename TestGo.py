__author__ = 'handwa'

from danian import gogame

def main():
    g = gogame.GoGame('W')
    g.play_move(('W',1,1))
    g.play_move(('W',3,1))
    g.play_move(('W',2,2))
    g.play_move(('W',1,2))
    g.play_move(('W',3,2))
    g.play_move(('W',3,3))
    g.play_move(('W',1,3))
    g.play_move(('W',3,4))
    g.play_move(('W',1,4))
    g.play_move(('W',2,4))
    g.play_move(('W',0,2))
    g.play_move(('B',0,1))
    g.play_move(('B',0,3))
    g.play_move(('B',0,4))
    g.play_move(('B',1,0))
    g.play_move(('B',1,5))
    g.play_move(('B',2,1))
    g.play_move(('B',2,5))
    g.play_move(('B',3,0))
    g.play_move(('B',3,5))
    g.play_move(('B',4,1))
    g.play_move(('B',4,2))
    g.play_move(('B',4,3))
    g.play_move(('B',4,4))
    g.print_board()
    print("")
    g.play_move(('B',2,3))

    g.print_board()


if __name__ == '__main__':
    main()