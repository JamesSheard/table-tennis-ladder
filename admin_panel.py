class admin:
    table = []

    def __init__(self):
        self.read_state()

    def read_state(self):
        try:
            f = open("ladder/ladder_state.txt")
            contents = f.read().split("\n")
            for line in contents:
                self.table.append(player(line))
            f.close()
            print len(self.table)

        except:
            self.table = []
            print "Could not find populated state file."



    def remove_player(self, remove_player):
        for player in self.table:
            if remove_player == player.name:
                self.table.pop(self.table.index(player))
                print "Player has been deleted"
                break
        else:
            print "Player does not exist in the ladder"

    def write_state(self):
        f = open("ladder/ladder_state.txt", "w+")
        f.truncate(0)
        for player in self.table:
            if self.table.index(player) == len(self.table) - 1:
                f.write(player.name)
            else:
                f.write(player.name + "\n")

        f.close()
        return

class admin_panel:

    def __init__(self):
        self.admin_panel = admin()

    def create_admin_menu(self, ladd):
        print "Would you like to: \n1. Remove Player \n2. Change player name \n3. Edit player position"
        admin_selection = raw_input("Please enter your selection: ")

        if admin_selection == "1":
            admin_remove_name = raw_input("Please enter the name of the player you would like to remove: ")
            self.admin_panel.remove_player(admin_remove_name)
        elif admin_selection == "2":
            admin_pos_name = raw_input("Please enter the name of the player you would like to remove: ")
            admin_pos_move = raw_input("Please enter the new position of the player: ")
            self.admin_panel.admin_move_pos(admin_pos_name, admin_pos_move)
        elif admin_selection == "3":
            print "3"

        self.admin_panel.write_state()