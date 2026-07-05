import sys
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

st.set_page_config(
    page_title="Football Prediction AI",
    page_icon="⚽",
    layout="wide",
)

st.title("⚽ Football Prediction AI")

st.markdown(
    """
    ### International Football Analytics Platform

    Predict football matches using:

    - ⚡ Elo Ratings
    - 🤖 Machine Learning
    - ⚽ Goal Prediction
    - 🎲 Monte Carlo Tournament Simulation
    """
)

st.divider()

# --------------------------------------------------
# Load Data
# --------------------------------------------------

ratings = pd.read_csv("outputs/team_ratings.csv")
matches = pd.read_csv("data/processed/results_clean.csv")

ratings = ratings.sort_values(
    "elo",
    ascending=False,
)

# --------------------------------------------------
# Metrics
# --------------------------------------------------

top_team = ratings.iloc[0]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "🌍 Teams",
    len(ratings),
)

col2.metric(
    "⚽ Matches",
    f"{len(matches):,}",
)

col3.metric(
    "🏆 Highest Rated",
    top_team["team"],
)

col4.metric(
    "⭐ Elo",
    f"{top_team['elo']:.0f}",
)

st.divider()

# --------------------------------------------------
# Top 10 Teams
# --------------------------------------------------

st.subheader("🏆 Top 10 Elo Rankings")

top10 = ratings.head(10).copy()

top10.insert(
    0,
    "Rank",
    range(1, 11),
)

top10 = top10.rename(
    columns={
        "team": "Team",
        "elo": "Elo Rating",
    }
)

st.dataframe(
    top10,
    hide_index=True,
    use_container_width=True,
)

st.divider()

# --------------------------------------------------
# Project Overview
# --------------------------------------------------

st.subheader("📊 Project Overview")

st.info(
    """
This project predicts international football matches using:

• Historical match results (1872–Present)

• Elo Rating System

• Machine Learning Goal Prediction

• Poisson Goal Simulation

• Monte Carlo Tournament Simulation
"""
)

st.divider()

# --------------------------------------------------
# Navigation
# --------------------------------------------------

st.subheader("🚀 Explore")

c1, c2 = st.columns(2)

with c1:

    st.success("⚽ Match Predictor")

    st.success("📊 Team Analysis")

    st.success("⚔️ Head-to-Head")

with c2:

    st.success("🏆 Elo Rankings")

    st.success("📈 Model Performance")

    st.success("🌍 Tournament Simulator")

st.divider()

st.caption(
    "Built by Rudraksh Prajapati • Ahmedabad University"
)