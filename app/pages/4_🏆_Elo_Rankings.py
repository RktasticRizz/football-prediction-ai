import sys
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

st.set_page_config(
    page_title="Elo Rankings",
    page_icon="🏆",
    layout="wide",
)

st.title("🏆 World Elo Rankings")

# -------------------------
# Load Ratings
# -------------------------

ratings = pd.read_csv("outputs/team_ratings.csv")

ratings = (
    ratings
    .sort_values("elo", ascending=False)
    .reset_index(drop=True)
)

# -------------------------
# Top Team Card
# -------------------------

top_team = ratings.iloc[0]

st.success(
    f"🌍 Current Highest Rated Team: **{top_team['team']}** "
    f"({top_team['elo']:.1f})"
)

ratings.index += 1

# -------------------------
# Sidebar Filters
# -------------------------

st.sidebar.header("Filters")

top_n = st.sidebar.slider(
    "Number of Teams",
    min_value=10,
    max_value=len(ratings),
    value=25,
)

search = st.sidebar.text_input(
    "Search Team",
).strip()

# -------------------------
# Filter Data
# -------------------------

display = ratings.copy()

if search:
    display = display[
        display["team"].str.contains(
            search,
            case=False,
            na=False,
        )
    ]

display = display.head(top_n)

display = display.rename(
    columns={
        "team": "Team",
        "elo": "Elo Rating",
    }
)

display.insert(
    0,
    "Rank",
    range(1, len(display) + 1),
)

# -------------------------
# Table
# -------------------------

st.dataframe(
    display,
    use_container_width=True,
    hide_index=True,
)

# -------------------------
# Download Button
# -------------------------

csv = display.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Rankings",
    data=csv,
    file_name="elo_rankings.csv",
    mime="text/csv",
)