import sys

class player:
    name = ""
    position = 0

    def __init__(self, name, position):
        self.name = name
        self.position = position


def main():
    if sys.argv[1] == "--name":
        name = sys.argv[2]
        position = sys.argv[4]
        player(name, position)
    else if sys.argv[1] == "--position":
        position = sys.argv[2]
        name = sys.argv[4]

    print player.name
    print player.position


        

    print james.name, james.position


#if __name__ == "__main__":
#    main()