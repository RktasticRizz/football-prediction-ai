import pandas as pd

from src.models.poisson import PoissonModel

from src.models.probability import ProbabilityModel


# Load ratings
ratings = pd.read_csv("outputs/team_ratings.csv")

ratings = ratings.set_index("team")


home_team = input("Home Team: ")
away_team = input("Away Team: ")


home_elo = ratings.loc[home_team]["elo"]
away_elo = ratings.loc[away_team]["elo"]


features = pd.DataFrame(
    [
        {
            "home_elo": home_elo,
            "away_elo": away_elo,
            "elo_difference": home_elo - away_elo,
            "neutral": False,
        }
    ]
)


model = PoissonModel()

model.load()


home_goals, away_goals = model.predict(features)

probability = ProbabilityModel()

home_win, draw, away_win, scores = probability.predict(
    home_goals,
    away_goals,
)

print("=" * 50)
print(f"{home_team} vs {away_team}")
print("=" * 50)

print()

print(f"Expected Goals")

print(f"{home_team:15} {home_goals:.2f}")
print(f"{away_team:15} {away_goals:.2f}")

print()

print("Winning Chances")

print(f"{home_team:15} {home_win*100:.1f}%")
print(f"Draw{'':11} {draw*100:.1f}%")
print(f"{away_team:15} {away_win*100:.1f}%")

print()

print("Most Likely Scores")

for home, away, p in scores[:5]:

    print(
        f"{home}-{away} : {p*100:.2f}%"
    )