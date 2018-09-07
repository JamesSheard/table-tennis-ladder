

class player:
    name = ""
    position = 0

    def __init__(self, name, position):
        self.name = name
        self.position = position


def main():
    james = player("james", 1)

    print james.name, james.position


if __name__ == "__main__":
    main()