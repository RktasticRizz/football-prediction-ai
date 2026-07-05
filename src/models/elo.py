from math import pow


class EloModel:
    """
    Basic Elo rating model.
    """

    def __init__(self, initial_rating=1500, k_factor=30):
        self.initial_rating = initial_rating
        self.k_factor = k_factor

    def expected_score(self, rating_a, rating_b):
        """
        Probability that Team A beats Team B.
        """
        return 1 / (1 + pow(10, (rating_b - rating_a) / 400))


    def update_rating(self, rating, expected, actual):
        """
        Update Elo rating.

        actual:
            1.0 = win
            0.5 = draw
            0.0 = loss
        """
        return rating + self.k_factor * (actual - expected)
    
