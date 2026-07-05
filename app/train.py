import pandas as pd
from sklearn.metrics import mean_absolute_error

from src.models.poisson import PoissonModel

# -------------------------
# Load Training Data
# -------------------------

print("📂 Loading training data...")

df = pd.read_csv("outputs/training_data.csv")

print(f"Loaded {len(df):,} matches")

# -------------------------
# Train Model
# -------------------------

print("🤖 Training goal prediction model...")

model = PoissonModel()

model.train(df)

# -------------------------
# Save Model
# -------------------------

model.save()

print("💾 Models saved.")

# -------------------------
# Generate Predictions
# -------------------------

print("📊 Generating predictions...")

df["pred_home"] = model.home_model.predict(
    df[model.features]
)

df["pred_away"] = model.away_model.predict(
    df[model.features]
)

# -------------------------
# Evaluate Model
# -------------------------

home_mae = mean_absolute_error(
    df["home_score"],
    df["pred_home"],
)

away_mae = mean_absolute_error(
    df["away_score"],
    df["pred_away"],
)

print("\n📈 Model Performance")
print("-" * 30)
print(f"Home Goal MAE : {home_mae:.3f}")
print(f"Away Goal MAE : {away_mae:.3f}")

# -------------------------
# Save Predictions
# -------------------------

df.to_csv(
    "outputs/model_predictions.csv",
    index=False,
)

print("\n✅ Training Finished!")
print("📁 Saved -> outputs/model_predictions.csv")