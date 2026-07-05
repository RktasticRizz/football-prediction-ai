from src.models.elo_engine import EloEngine

engine = EloEngine()

ratings = engine.fit()

engine.save_ratings()
engine.save_history()
engine.save_training_data()

print("\nTop 10 Teams\n")

top_10 = sorted(
    ratings.items(),
    key=lambda x: x[1],
    reverse=True,
)[:10]

for rank, (team, rating) in enumerate(top_10, start=1):
    print(f"{rank:2d}. {team:<20} {rating:.2f}")