from collections import defaultdict, deque
import pandas as pd


class FeatureBuilder:
    """
    Builds machine learning features from historical matches.
    """

    def __init__(self):
        # Last 5 match results (3 = Win, 1 = Draw, 0 = Loss)
        self.form = defaultdict(lambda: deque(maxlen=5))

        # Goals scored in last 10 matches
        self.goals_for = defaultdict(lambda: deque(maxlen=10))

        # Goals conceded in last 10 matches
        self.goals_against = defaultdict(lambda: deque(maxlen=10))

        # Stores all generated feature rows
        self.training_rows = []

    def get_recent_form(self, team):
        """
        Returns recent form between 0 and 1.
        """

        history = self.form[team]

        if len(history) == 0:
            return 0.5

        return sum(history) / (3 * len(history))

    def get_attack_strength(self, team):
        """
        Average goals scored over recent matches.
        """

        history = self.goals_for[team]

        if len(history) == 0:
            return 1.0

        return sum(history) / len(history)

    def get_defense_strength(self, team):
        """
        Average goals conceded over recent matches.
        Lower is better.
        """

        history = self.goals_against[team]

        if len(history) == 0:
            return 1.0

        return sum(history) / len(history)

    def update(
        self,
        home_team,
        away_team,
        home_score,
        away_score,
    ):
        """
        Update feature history after a match.
        """

        # -----------------------------
        # Goals scored / conceded
        # -----------------------------

        self.goals_for[home_team].append(home_score)
        self.goals_against[home_team].append(away_score)

        self.goals_for[away_team].append(away_score)
        self.goals_against[away_team].append(home_score)

        # -----------------------------
        # Recent form
        # -----------------------------

        if home_score > away_score:
            self.form[home_team].append(3)
            self.form[away_team].append(0)

        elif home_score < away_score:
            self.form[home_team].append(0)
            self.form[away_team].append(3)

        else:
            self.form[home_team].append(1)
            self.form[away_team].append(1)