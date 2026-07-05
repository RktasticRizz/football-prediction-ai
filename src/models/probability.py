from scipy.stats import poisson


class ProbabilityModel:
    """
    Computes match outcome probabilities using the Poisson distribution.
    """

    def __init__(self, max_goals=6):
        self.max_goals = max_goals

    def predict(self, home_lambda, away_lambda):

        home_win = 0.0
        draw = 0.0
        away_win = 0.0

        score_probs = []

        for home_goals in range(self.max_goals + 1):

            for away_goals in range(self.max_goals + 1):

                probability = (
                    poisson.pmf(home_goals, home_lambda)
                    * poisson.pmf(away_goals, away_lambda)
                )

                score_probs.append(
                    (
                        home_goals,
                        away_goals,
                        probability,
                    )
                )

                if home_goals > away_goals:
                    home_win += probability

                elif home_goals == away_goals:
                    draw += probability

                else:
                    away_win += probability

        score_probs.sort(
            key=lambda x: x[2],
            reverse=True,
        )

        return (
            home_win,
            draw,
            away_win,
            score_probs,
        )