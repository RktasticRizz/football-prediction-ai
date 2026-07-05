import pandas as pd
import streamlit as st

from src.simulation.tournament import TournamentSimulator

st.set_page_config(
    page_title="Tournament Simulator",
    page_icon="🏆",
    layout="wide",
)

st.title("🏆 Tournament Simulator")

ratings = pd.read_csv(
    "outputs/team_ratings.csv"
)

teams = sorted(ratings["team"])

selected = st.multiselect(
    "Select 8 Teams",
    teams,
    default=[
        "Brazil",
        "Argentina",
        "France",
        "England",
        "Spain",
        "Portugal",
        "Germany",
        "Netherlands",
    ],
)

if len(selected) != 8:

    st.warning("Please select exactly 8 teams.")

    st.stop()

simulator = TournamentSimulator()

col1, col2 = st.columns(2)

with col1:

    if st.button("🏆 Simulate Tournament"):

        tournament = simulator.simulate(selected)

        rounds = [
            "Quarter Finals",
            "Semi Finals",
            "Final",
        ]

        for name, matches in zip(
            rounds,
            tournament["history"],
        ):

            st.subheader(name)

            for match in matches:

                st.write(
                    f"**{match['home_team']} {match['home_score']} - {match['away_score']} {match['away_team']}**"
                )

                st.success(
                    f"Winner: {match['winner']}"
                )

        st.balloons()

        st.header(
            f"🏆 Champion: {tournament['champion']}"
        )

with col2:

    if st.button("🎲 Simulate 1000 Tournaments"):

        champions = simulator.simulate_many(
            selected,
            simulations=1000,
        )

        champion_df = (
            pd.DataFrame(
                champions.items(),
                columns=[
                    "Team",
                    "Titles",
                ],
            )
            .sort_values(
                "Titles",
                ascending=False,
            )
        )

        champion_df["Probability"] = (
            champion_df["Titles"] / 1000 * 100
        ).round(2)

        st.dataframe(
            champion_df,
            use_container_width=True,
            hide_index=True,
        )