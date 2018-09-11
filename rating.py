import math


class Rating:
    def __init__(self):
        self.K = 100

    def probability(self, player_a_rating, player_b_rating):
        return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (player_a_rating - player_b_rating) / 400))

    def calculate_rating(self, player_a_rating, player_b_rating, first_player_win, draw):
        probability_player_a = self.probability(player_a_rating, player_b_rating)
        probability_player_b = self.probability(player_b_rating, player_a_rating)

        if draw:
            return

        elif first_player_win:
            player_a_rating = player_a_rating + self.K * (1 - probability_player_a)
            player_b_rating = player_b_rating + self.K * (0 - probability_player_b)

        else:
            player_a_rating = player_a_rating + self.K * (0 - probability_player_a)
            player_b_rating = player_b_rating + self.K * (1 - probability_player_b)

        print "updated ratings:"
        print "player a: " + str(round(player_a_rating))
        print "player b: " + str(round(player_b_rating))


if __name__ == "__main__":
    rating = Rating()
    rating.calculate_rating(1500, 1500, True, False)