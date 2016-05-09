__author__ = 'handwa'
from danian import ogsession, gogame
import time

def main():
    session = ogsession.OGSession()
    f = open("games.txt",'w')
    #print(session.session_key)
    count = 0
    for i in range(0,2000):
        thing = session.get_games(i + 1)
        for game in thing['results']:
            if game['width'] == 9 and game['height'] == 9 and game['players']['white']['ranking'] >= 20 and game['players']['black']['ranking'] >= 20 and game['outcome'] != '':
                f.write(str(game['id']) + "\n")
                count += 1
        print("FOUND " + str(count) + " GAMES AT PAGE " + str(i+1))
    print("FOUND " + str(count) + " GAMES")
    f.close()


if __name__=='__main__':
    main()
