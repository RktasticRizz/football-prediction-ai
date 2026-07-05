from random import random

from src.services.predictor import MatchPredictor


class MatchSimulator:

    def __init__(self):
        self.predictor = MatchPredictor()

    def play(self, home_team, away_team, neutral=True):

        prediction = self.predictor.predict(
            home_team,
            away_team,
            neutral,
        )

        # Most likely scoreline
        home_score, away_score, _ = prediction["scores"][0]

        r = random()

        if r < prediction["home_win"]:
            winner = home_team

        elif r < prediction["home_win"] + prediction["draw"]:
            winner = home_team if random() < 0.5 else away_team

        else:
            winner = away_team

        return {
            "home_team": home_team,
            "away_team": away_team,
            "home_score": home_score,
            "away_score": away_score,
            "winner": winner,
        }