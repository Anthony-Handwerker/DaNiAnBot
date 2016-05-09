__author__ = 'handwa'

from danian import ogsession

def main():
    session = ogsession.OGSession()
    f = open("games.txt",'r')
    i = 0
    for line in f:
        l = line[:-1]
        f2 = open("training_data/" + l + ".txt", 'w')
        try:
            s = session.get_sgf(l)
            f2.write(s)
            f2.close()
        except:
            print("ERROR ON")
        print(i)
        i += 1
    f.close()

if __name__ == '__main__':
    main()