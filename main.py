import sys

class player:
    name = ""
    position = 0

    def __init__(self, name, position):
        self.name = name
        self.position = position


def main():
    p1 = player
    if sys.argv[1] == "--name":
        name = sys.argv[2]
        position = sys.argv[4]
        p1 = player(name, position)
    elif sys.argv[1] == "--position":
        position = sys.argv[2]
        name = sys.argv[4]
        p1(name, position)

    print p1.name
    print p1.position


if __name__ == "__main__":
    main()