from pathlib import Path

import pandas as pd

from src.models.elo import EloModel
from src.features.feature_builder import FeatureBuilder


class EloEngine:
    """
    Trains Elo ratings from historical international football matches.
    """

    def __init__(
        self,
        data_path: Path = Path("data/processed/results_clean.csv"),
    ):
        self.data_path = data_path

        self.elo = EloModel()
        self.features = FeatureBuilder()

        # Current Elo ratings
        self.ratings = {}

        # Rating history
        self.rating_history = []

        # Machine Learning dataset
        self.training_data = []

    def get_rating(self, team: str) -> float:
        """
        Return a team's current Elo rating.
        """

        if team not in self.ratings:
            self.ratings[team] = self.elo.initial_rating

        return self.ratings[team]

    def process_match(
        self,
        date,
        home_team,
        away_team,
        home_score,
        away_score,
        tournament,
        neutral,
    ):
        """
        Process one historical match.
        """

        # -----------------------
        # Ratings BEFORE match
        # -----------------------

        home_rating = self.get_rating(home_team)
        away_rating = self.get_rating(away_team)

        # -----------------------
        # Save ML features BEFORE updating
        # -----------------------

        self.training_data.append(
            {
                "date": date,

                "home_team": home_team,
                "away_team": away_team,

                "home_elo": home_rating,
                "away_elo": away_rating,
                "elo_difference": home_rating - away_rating,

                "home_form": self.features.get_recent_form(home_team),
                "away_form": self.features.get_recent_form(away_team),

                "home_attack": self.features.get_attack_strength(home_team),
                "away_attack": self.features.get_attack_strength(away_team),

                "home_defense": self.features.get_defense_strength(home_team),
                "away_defense": self.features.get_defense_strength(away_team),

                "neutral": neutral,
                "tournament": tournament,

                "home_score": home_score,
                "away_score": away_score,
            }
        )

        # -----------------------
        # Expected Result
        # -----------------------

        home_expected = self.elo.expected_score(
            home_rating,
            away_rating,
        )

        away_expected = self.elo.expected_score(
            away_rating,
            home_rating,
        )

        # -----------------------
        # Actual Result
        # -----------------------

        if home_score > away_score:

            home_actual = 1.0
            away_actual = 0.0

        elif away_score > home_score:

            home_actual = 0.0
            away_actual = 1.0

        else:

            home_actual = 0.5
            away_actual = 0.5

        # -----------------------
        # Update Ratings
        # -----------------------

        new_home_rating = self.elo.update_rating(
            home_rating,
            home_expected,
            home_actual,
        )

        new_away_rating = self.elo.update_rating(
            away_rating,
            away_expected,
            away_actual,
        )

        self.ratings[home_team] = new_home_rating
        self.ratings[away_team] = new_away_rating

        # -----------------------
        # Save Rating History
        # -----------------------

        self.rating_history.append(
            {
                "date": date,
                "team": home_team,
                "elo": new_home_rating,
            }
        )

        self.rating_history.append(
            {
                "date": date,
                "team": away_team,
                "elo": new_away_rating,
            }
        )

        # -----------------------
        # Update Feature History
        # -----------------------

        self.features.update(
            home_team=home_team,
            away_team=away_team,
            home_score=home_score,
            away_score=away_score,
        )

    def fit(self):
        """
        Train Elo ratings using all historical matches.
        """

        df = pd.read_csv(self.data_path)

        df["date"] = pd.to_datetime(df["date"])

        df = df.sort_values("date")

        print(f"Processing {len(df):,} matches...\n")

        for _, match in df.iterrows():

            self.process_match(
                date=match["date"],
                home_team=match["home_team"],
                away_team=match["away_team"],
                home_score=match["home_score"],
                away_score=match["away_score"],
                tournament=match["tournament"],
                neutral=match["neutral"],
            )

        print("Training Complete!")

        return self.ratings

    def save_ratings(
        self,
        output_path: Path = Path("outputs/team_ratings.csv"),
    ):
        """
        Save latest Elo ratings.
        """

        ratings = pd.DataFrame(
            [
                {
                    "team": team,
                    "elo": rating,
                }
                for team, rating in self.ratings.items()
            ]
        )

        ratings = ratings.sort_values(
            "elo",
            ascending=False,
        )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        ratings.to_csv(
            output_path,
            index=False,
        )

        print(f"Saved ratings -> {output_path}")

    def save_history(
        self,
        output_path: Path = Path("outputs/elo_history.csv"),
    ):
        """
        Save complete Elo history.
        """

        history = pd.DataFrame(
            self.rating_history
        )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        history.to_csv(
            output_path,
            index=False,
        )

        print(f"Saved history -> {output_path}")

    def save_training_data(
        self,
        output_path: Path = Path("outputs/training_data.csv"),
    ):
        """
        Save ML dataset.
        """

        training = pd.DataFrame(
            self.training_data
        )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        training.to_csv(
            output_path,
            index=False,
        )

        print(f"Saved training data -> {output_path}")