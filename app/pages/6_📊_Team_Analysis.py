import sys
from pathlib import Path

import pandas as pd
import streamlit as st
import plotly.express as px

ROOT = Path(__file__).resolve().parent.parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

st.set_page_config(
    page_title="Team Analysis",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Team Analysis")

# --------------------------
# Load Data
# --------------------------

ratings = pd.read_csv("outputs/team_ratings.csv")
history = pd.read_csv("outputs/elo_history.csv")
matches = pd.read_csv("data/processed/results_clean.csv")

teams = sorted(ratings["team"].unique())

team = st.selectbox(
    "Select Team",
    teams,
)

# --------------------------
# Current Rating
# --------------------------

current_rating = ratings.loc[
    ratings["team"] == team,
    "elo"
].iloc[0]

# --------------------------
# Match History
# --------------------------

team_matches = matches[
    (matches["home_team"] == team) |
    (matches["away_team"] == team)
].copy()

matches_played = len(team_matches)

wins = 0
draws = 0
losses = 0

goals_for = 0
goals_against = 0

for _, row in team_matches.iterrows():

    if row["home_team"] == team:

        gf = row["home_score"]
        ga = row["away_score"]

    else:

        gf = row["away_score"]
        ga = row["home_score"]

    goals_for += gf
    goals_against += ga

    if gf > ga:
        wins += 1

    elif gf == ga:
        draws += 1

    else:
        losses += 1

win_rate = wins / matches_played * 100

avg_scored = goals_for / matches_played
avg_conceded = goals_against / matches_played

# --------------------------
# Metrics
# --------------------------

st.subheader(team)

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Current Elo",
    f"{current_rating:.0f}",
)

c2.metric(
    "Matches",
    matches_played,
)

c3.metric(
    "Win %",
    f"{win_rate:.1f}",
)

c4.metric(
    "Goals / Match",
    f"{avg_scored:.2f}",
)

st.divider()

c1, c2, c3 = st.columns(3)

c1.metric(
    "Wins",
    wins,
)

c2.metric(
    "Draws",
    draws,
)

c3.metric(
    "Losses",
    losses,
)

st.divider()

# --------------------------
# Elo History
# --------------------------

st.subheader("📈 Elo Rating History")

team_history = history[
    history["team"] == team
].copy()

team_history["date"] = pd.to_datetime(team_history["date"])

fig = px.line(
    team_history,
    x="date",
    y="elo",
    markers=False,
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

# --------------------------
# Last Matches
# --------------------------

st.subheader("Recent Matches")

st.dataframe(
    team_matches.sort_values("date", ascending=False)
    .head(10),
    use_container_width=True,
)