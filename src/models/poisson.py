import joblib
from sklearn.ensemble import RandomForestRegressor


class PoissonModel:

    def __init__(self):

        self.features = [
            "home_elo",
            "away_elo",
            "elo_difference",
            "neutral",
        ]

        # Home Goals Model
        self.home_model = RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            min_samples_leaf=5,
            random_state=42,
            n_jobs=-1,
        )

        # Away Goals Model
        self.away_model = RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            min_samples_leaf=5,
            random_state=42,
            n_jobs=-1,
        )

    def train(self, df):
        """
        Train both goal prediction models.
        """

        X = df[self.features]

        y_home = df["home_score"]
        y_away = df["away_score"]

        self.home_model.fit(X, y_home)
        self.away_model.fit(X, y_away)

    def predict(self, features):
        """
        Predict expected home and away goals.
        """

        X = features[self.features]

        home_goals = self.home_model.predict(X)[0]
        away_goals = self.away_model.predict(X)[0]

        return float(home_goals), float(away_goals)

    def save(self):
        """
        Save trained models.
        """

        joblib.dump(
            self.home_model,
            "outputs/home_model.pkl",
            compress=3,
        )

        joblib.dump(
            self.away_model,
            "outputs/away_model.pkl",
            compress=3,
        )

    def load(self):
        """
        Load trained models.
        """

        self.home_model = joblib.load(
            "outputs/home_model.pkl"
        )

        self.away_model = joblib.load(
            "outputs/away_model.pkl"
        )