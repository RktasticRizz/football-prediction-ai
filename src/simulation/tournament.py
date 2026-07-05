import random

from src.simulation.match import MatchSimulator


class TournamentSimulator:

    def __init__(self):
        self.match = MatchSimulator()

    def simulate(self, teams):

        current_round = teams.copy()

        random.shuffle(current_round)

        history = []

        round_names = {
            2: "Final",
            4: "Semi Finals",
            8: "Quarter Finals",
            16: "Round of 16",
            32: "Round of 32",
        }

        while len(current_round) > 1:

            matches = []
            winners = []

            for i in range(0, len(current_round), 2):

                result = self.match.play(
                    current_round[i],
                    current_round[i + 1],
                )

                matches.append(result)

                winners.append(result["winner"])

            history.append(
                {
                    "round": round_names[len(current_round)],
                    "matches": matches,
                }
            )

            current_round = winners

        return {
            "champion": current_round[0],
            "history": history,
        }

    def simulate_many(
        self,
        teams,
        simulations=1000,
    ):

        champions = {}

        for _ in range(simulations):

            result = self.simulate(teams)

            champion = result["champion"]

            champions[champion] = (
                champions.get(champion, 0) + 1
            )

        return champions