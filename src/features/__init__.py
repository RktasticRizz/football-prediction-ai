from collections import defaultdict, deque
import pandas as pd


class FeatureBuilder:
    """
    Builds machine learning features from historical matches.
    """

    def __init__(self):

        self.form = defaultdict(lambda: deque(maxlen=5))

        self.goals_for = defaultdict(lambda: deque(maxlen=10))

        self.goals_against = defaultdict(lambda: deque(maxlen=10))

        self.training_rows = []

    def get_recent_form(self, team):
        ...
    
    def get_attack_strength(self, team):
        ...

    def get_defense_strength(self, team):
        ...