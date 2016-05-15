__author__ = 'handwa'
from danian import ogsession, gogame
import time
import re

def main():
    session = ogsession.OGSession()
    f = open("games.txt",'w')
    #print(session.session_key)
    count = 0
    for i in range(0,1000):
        thing = session.get_games(i + 1)
        for game in thing['results']:
            try:
                if game['width'] == 9 and game['height'] == 9 and game['outcome'] != '':
                    thing2 = session.get_sgf(game['id'])
                    black_rank = re.search('BR\[(.*)\]', thing2).group(1)
                    white_rank = re.search('WR\[(.*)\]', thing2).group(1)
                    if test_rank(black_rank) and test_rank(white_rank):
                        f2 = open("training_data/" + str(game['id']) + ".sgf", 'w')
                        f2.write(thing2)
                        f2.close()
                        count += 1
            except:
                print("ERROR!")
        print("FOUND " + str(count) + " GAMES AT PAGE " + str(i+1))
    print("FOUND " + str(count) + " GAMES")
    f.close()

def test_rank(test):
    typ = test[-1]
    if typ == 'd' or typ == 'p':
        return True
    num = int(test[:-1])
    return num <= 10

if __name__=='__main__':
    main()


