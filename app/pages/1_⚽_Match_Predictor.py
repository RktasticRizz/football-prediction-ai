import sys
from pathlib import Path

import pandas as pd
import streamlit as st

# -----------------------------
# Fix imports
# -----------------------------

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.services.predictor import MatchPredictor

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Football Prediction AI",
    page_icon="⚽",
    layout="wide",
)

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.title("⚽ Football Prediction AI")

    st.markdown("---")

    st.subheader("Model")

    st.write("✅ Elo Rating")
    st.write("✅ Goal Prediction")
    st.write("✅ Poisson Simulation")

    st.markdown("---")

    st.subheader("Dataset")

    st.write("📅 1872 – Present")
    st.write("⚽ ~49,000 Matches")

    st.markdown("---")

    st.caption("Built with Python + Streamlit")

# -----------------------------
# Main Title
# -----------------------------

st.title("⚽ Football Match Predictor")

st.write(
    "Predict international football matches using historical results, Elo ratings and machine learning."
)

st.divider()

# -----------------------------
# Load Data
# -----------------------------

ratings = pd.read_csv("outputs/team_ratings.csv")

teams = sorted(ratings["team"])

# -----------------------------
# Team Selection
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    home_team = st.selectbox(
        "🏠 Home Team",
        teams,
        index=teams.index("Brazil") if "Brazil" in teams else 0,
    )

with col2:

    away_team = st.selectbox(
        "✈️ Away Team",
        teams,
        index=teams.index("Argentina") if "Argentina" in teams else 1,
    )

neutral = st.checkbox(
    "Neutral Venue",
    value=False,
)

# -----------------------------
# Prediction Button
# -----------------------------

if st.button("🔮 Predict Match", use_container_width=True):

    predictor = MatchPredictor()

    result = predictor.predict(
        home_team=home_team,
        away_team=away_team,
        neutral=neutral,
    )

    home_goals = result["home_goals"]
    away_goals = result["away_goals"]

    home_elo = result["home_elo"]
    away_elo = result["away_elo"]

    home_win = result["home_win"]
    draw = result["draw"]
    away_win = result["away_win"]

    scores = result["scores"]

    st.divider()

    # -----------------------------
    # Expected Goals
    # -----------------------------

    st.subheader("⚽ Expected Goals")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(home_team, f"{home_goals:.2f}")

    with c2:
        st.metric(away_team, f"{away_goals:.2f}")

    # -----------------------------
    # Elo Ratings
    # -----------------------------

    st.subheader("📈 Current Elo Ratings")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(home_team, f"{int(home_elo)}")

    with c2:
        st.metric(away_team, f"{int(away_elo)}")

    # -----------------------------
    # Win Probability
    # -----------------------------

    st.subheader("🏆 Match Outcome Probability")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(home_team, f"{home_win*100:.1f}%")
        st.progress(float(home_win))

    with c2:
        st.metric("Draw", f"{draw*100:.1f}%")
        st.progress(float(draw))

    with c3:
        st.metric(away_team, f"{away_win*100:.1f}%")
        st.progress(float(away_win))

    # -----------------------------
    # Most Likely Scorelines
    # -----------------------------

    st.subheader("🎯 Most Likely Scorelines")

    score_df = pd.DataFrame(
        scores[:10],
        columns=[
            "Home Goals",
            "Away Goals",
            "Probability",
        ],
    )

    score_df["Score"] = (
        score_df["Home Goals"].astype(str)
        + " - "
        + score_df["Away Goals"].astype(str)
    )

    score_df["Probability"] = (
        score_df["Probability"] * 100
    ).round(2)

    st.dataframe(
        score_df[["Score", "Probability"]],
        hide_index=True,
        use_container_width=True,
    )