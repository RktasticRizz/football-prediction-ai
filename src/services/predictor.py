import pandas as pd

from src.models.poisson import PoissonModel
from src.models.probability import ProbabilityModel


class MatchPredictor:
    """
    Predicts the outcome of a football match using
    Elo ratings + Goal Model + Poisson simulation.
    """

    def __init__(self):

        self.ratings = pd.read_csv(
            "outputs/team_ratings.csv"
        ).set_index("team")

        self.goal_model = PoissonModel()
        self.goal_model.load()

        self.probability_model = ProbabilityModel()

    def predict(
        self,
        home_team,
        away_team,
        neutral=False,
    ):

        home_elo = self.ratings.loc[home_team]["elo"]
        away_elo = self.ratings.loc[away_team]["elo"]

        features = pd.DataFrame(
            [
                {
                    "home_elo": home_elo,
                    "away_elo": away_elo,
                    "elo_difference": home_elo - away_elo,
                    "neutral": neutral,
                }
            ]
        )

        home_goals, away_goals = self.goal_model.predict(
            features
        )

        home_win, draw, away_win, scores = (
            self.probability_model.predict(
                home_goals,
                away_goals,
            )
        )

        return {
            "home_team": home_team,
            "away_team": away_team,
            "home_elo": home_elo,
            "away_elo": away_elo,
            "home_goals": home_goals,
            "away_goals": away_goals,
            "home_win": home_win,
            "draw": draw,
            "away_win": away_win,
            "scores": scores,
        }