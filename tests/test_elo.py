from src.models.elo import EloModel

elo = EloModel()

print("=" * 50)
print("EXPECTED SCORE TESTS")
print("=" * 50)

print(elo.expected_score(1500, 1500))
print(elo.expected_score(1700, 1500))
print(elo.expected_score(1500, 1700))

print("=" * 50)
print("RATING UPDATE TEST")
print("=" * 50)

rating = 1500
expected = elo.expected_score(1500, 1500)

new_rating = elo.update_rating(
    rating=rating,
    expected=expected,
    actual=1.0,
)

print(new_rating)