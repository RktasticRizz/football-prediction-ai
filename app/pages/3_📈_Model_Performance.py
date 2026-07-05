import sys
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
)

ROOT = Path(__file__).resolve().parent.parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide",
)

st.title("📈 Goal Prediction Model Performance")

# --------------------------
# Load Data
# --------------------------

df = pd.read_csv(
    "outputs/model_predictions.csv"
)

# --------------------------
# Metrics
# --------------------------

home_mae = mean_absolute_error(
    df["home_score"],
    df["pred_home"],
)

away_mae = mean_absolute_error(
    df["away_score"],
    df["pred_away"],
)

home_rmse = mean_squared_error(
    df["home_score"],
    df["pred_home"],
) ** 0.5

away_rmse = mean_squared_error(
    df["away_score"],
    df["pred_away"],
) ** 0.5

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Home MAE",
    f"{home_mae:.3f}",
)

c2.metric(
    "Away MAE",
    f"{away_mae:.3f}",
)

c3.metric(
    "Home RMSE",
    f"{home_rmse:.3f}",
)

c4.metric(
    "Away RMSE",
    f"{away_rmse:.3f}",
)

st.divider()

# --------------------------
# Scatter Plot
# --------------------------

st.subheader("⚽ Actual vs Predicted (Home Goals)")

fig = px.scatter(
    df,
    x="home_score",
    y="pred_home",
    opacity=0.35,
    trendline="ols",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

st.subheader("⚽ Actual vs Predicted (Away Goals)")

fig = px.scatter(
    df,
    x="away_score",
    y="pred_away",
    opacity=0.35,
    trendline="ols",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

# --------------------------
# Error Distribution
# --------------------------

df["home_error"] = (
    df["pred_home"]
    - df["home_score"]
)

st.subheader("📉 Home Goal Prediction Error")

fig = px.histogram(
    df,
    x="home_error",
    nbins=40,
)

st.plotly_chart(
    fig,
    use_container_width=True,
)