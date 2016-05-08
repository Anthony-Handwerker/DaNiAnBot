import danian.coreai as C

def main():
    ai = C.CoreAI()
    child1 = C.MCTreeNode()
    child2 = C.MCTreeNode()
    child3 = C.MCTreeNode()
    ai.root.add_child(child1)
    child1.add_child(child2)
    child1.add_child(child3)
    child2.wins = [1,0]
    child3.wins = [0,1]
    child2.back_propagate()
    print(ai.root.wins)
    print(child1.wins)
    child3.back_propagate()
    print(ai.root.wins)
    print(child1.wins)

if __name__ == '__main__':
    main()