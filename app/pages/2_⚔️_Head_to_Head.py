import sys
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.models.poisson import PoissonModel
from src.models.probability import ProbabilityModel

st.set_page_config(
    page_title="Head to Head",
    page_icon="⚔️",
    layout="wide",
)

st.title("⚔️ Head-to-Head Analysis")

# --------------------------
# Load Data
# --------------------------

matches = pd.read_csv("data/processed/results_clean.csv")
ratings = pd.read_csv("outputs/team_ratings.csv")

ratings = ratings.set_index("team")

teams = sorted(ratings.index.tolist())

col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox(
        "Team 1",
        teams,
        index=teams.index("Brazil") if "Brazil" in teams else 0,
    )

with col2:
    team2 = st.selectbox(
        "Team 2",
        teams,
        index=teams.index("Argentina") if "Argentina" in teams else 1,
    )

if team1 == team2:
    st.warning("Choose two different teams.")
    st.stop()

# --------------------------
# Historical Matches
# --------------------------

h2h = matches[
    (
        (matches["home_team"] == team1)
        & (matches["away_team"] == team2)
    )
    |
    (
        (matches["home_team"] == team2)
        & (matches["away_team"] == team1)
    )
]

team1_wins = 0
team2_wins = 0
draws = 0

team1_goals = 0
team2_goals = 0

for _, match in h2h.iterrows():

    if match["home_team"] == team1:

        g1 = match["home_score"]
        g2 = match["away_score"]

    else:

        g1 = match["away_score"]
        g2 = match["home_score"]

    team1_goals += g1
    team2_goals += g2

    if g1 > g2:
        team1_wins += 1

    elif g2 > g1:
        team2_wins += 1

    else:
        draws += 1

# --------------------------
# Prediction
# --------------------------

home_elo = ratings.loc[team1]["elo"]
away_elo = ratings.loc[team2]["elo"]

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

prob = ProbabilityModel()

home_win, draw, away_win, scores = prob.predict(
    home_goals,
    away_goals,
)

# --------------------------
# Summary Cards
# --------------------------

st.subheader(f"{team1} vs {team2}")

c1, c2, c3 = st.columns(3)

c1.metric(
    f"{team1} Wins",
    team1_wins,
)

c2.metric(
    "Draws",
    draws,
)

c3.metric(
    f"{team2} Wins",
    team2_wins,
)

st.divider()

c1, c2 = st.columns(2)

c1.metric(
    f"{team1} Goals",
    team1_goals,
)

c2.metric(
    f"{team2} Goals",
    team2_goals,
)

st.divider()

# --------------------------
# Prediction
# --------------------------

st.subheader("🔮 Prediction")

c1, c2 = st.columns(2)

c1.metric(team1, f"{home_goals:.2f}")
c2.metric(team2, f"{away_goals:.2f}")

st.write("### Win Probability")

st.progress(float(home_win))
st.write(f"**{team1}: {home_win*100:.1f}%**")

st.progress(float(draw))
st.write(f"**Draw: {draw*100:.1f}%**")

st.progress(float(away_win))
st.write(f"**{team2}: {away_win*100:.1f}%**")

st.divider()

# --------------------------
# Previous Meetings
# --------------------------

st.subheader("📅 Previous Meetings")

st.dataframe(
    h2h.sort_values("date", ascending=False),
    use_container_width=True,
)