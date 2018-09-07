import sys

class player:

    def __init__(self, name, position):
        self.name = name
        self.position = position

class ladder:
    table = []
    def __init__(self):
        self.table = []
    def get_ladder(self):
        return self.table



def main():
    p1 = player
    ladd = ladder()
    if sys.argv[1] == "--name":
        name = sys.argv[2]
        position = sys.argv[4]
        ladder.table.append(player(name, position))
    elif sys.argv[1] == "--position":
        position = sys.argv[2]
        name = sys.argv[4]
        ladder.table.append(player(name, position))
    elif sys.argv[1] == "--getladder":
        print ladd.get_ladder()


if __name__ == "__main__":
    main()