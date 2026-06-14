import streamlit as st
from games_data import games

st.title("⏱️ Game Timer")

game = st.selectbox(
    "Choose Game",
    list(games.keys())
)

times = {
    "Chess": 45,
    "Uno": 20,
    "Monopoly": 90,
    "Scrabble": 60,
    "Catan": 90,
    "Ticket to Ride": 45,
    "Jodo": 20,
    "Tangram": 15
}

st.metric(
    "Recommended Time",
    f"{times[game]} mins"
)

st.info(
    f"⏰ Suggested play time for {game}: {times[game]} minutes"
)