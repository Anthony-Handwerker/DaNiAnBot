#!/usr/bin/env python3
__author__ = 'handwa'
from danian import ogsession, gogame
import time
import re
import multiprocessing

def download_worker(url_and_target):
    '''
    Parallelize data download via multiprocessing
    '''
    try:
        (url, target_path) = url_and_target
        print('>>> Downloading ' + target_path)
        urllib.request.urlretrieve(url, target_path)
    except (KeyboardInterrupt, SystemExit):
        print('>>> Exiting child process')
def metadata_worker(games):
    count = 0
    for game in games:
        try:
            if game['width'] == 9 and game['height'] == 9 and game['outcome'] != '':
                thing2 = session.get_sgf(game['id'])
                urls_to_download.append((thing2, "training_data/" + str(game['id']) + ".sgf"))
                black_rank = re.search('BR\[(.*)\]', thing2).group(1)
                white_rank = re.search('WR\[(.*)\]', thing2).group(1)
                if test_rank(black_rank) and test_rank(white_rank):
                    f2 = open("training_data/" + str(game['id']) + ".sgf", 'w')
                    f2.write(thing2)
                    f2.close()
                    count += 1
        except:
            print("ERROR!")
    print("Downloaded " + str(i) + " games!")

def main():
    session = ogsession.OGSession()
    #print(session.session_key)
    count = 0
    # cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(16)
    game_pages = []
    for i in range(1, 200000):
        game_pages.append(session.get_games(i))
        if (i % 10 == 0):
            print("On page " + str(i))
        if (i % 100 == 0):
            print("On page " + str(i))
            pool = multiprocessing.Pool(16)
            try:
                it = pool.imap(metadata_worker, game_pages)
                for i in it:
                    pass
                pool.close()
                pool.join()
            except KeyboardInterrupt:
                print(">>> Caught KeyboardInterrupt, terminating workers")
                pool.terminate()
                pool.join()
                sys.exit(-1)
            game_pages = []


# def main():
#     session = ogsession.OGSession()
#     f = open("games.txt",'w')
#     #print(session.session_key)
#     count = 0
#     for i in range(0,1000):
#         thing = session.get_games(i + 1)
#         for game in thing['results']:
#             try:
#                 if game['width'] == 9 and game['height'] == 9 and game['outcome'] != '':
#                     thing2 = session.get_sgf(game['id'])
#                     urls_to_download.append((thing2))
#                     black_rank = re.search('BR\[(.*)\]', thing2).group(1)
#                     white_rank = re.search('WR\[(.*)\]', thing2).group(1)
#                     if test_rank(black_rank) and test_rank(white_rank):
#                         f2 = open("training_data/" + str(game['id']) + ".sgf", 'w')
#                         f2.write(thing2)
#                         f2.close()
#                         count += 1
#             except:
#                 print("ERROR!")
#         print("FOUND " + str(count) + " GAMES AT PAGE " + str(i+1))
#     print("FOUND " + str(count) + " GAMES")
#     f.close()

def test_rank(test):
    typ = test[-1]
    if typ == 'd' or typ == 'p':
        return True
    num = int(test[:-1])
    return num <= 10

if __name__=='__main__':
    main()


