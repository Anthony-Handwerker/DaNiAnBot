import os

def main():
    l = os.listdir('training_data')
    i = 0
    removed = 0
    for f in l:
        flag = False
        fil = open("training_data/" + f)
        for line in fil:
            i += 1
            flag = True
            break
        if not flag:
            os.remove("training_data/" + f)
            removed += 1
    print("REMOVED " + str(removed) + " AND KEPT " + str(i))

if __name__ == '__main__':
    main()