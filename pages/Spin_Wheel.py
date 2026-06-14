import streamlit as st
import random
from games_data import games

st.title("🎡 Spin The Wheel")

st.write("Can't decide what to play?")

if st.button("🎲 SPIN!"):

    winner = random.choice(
        list(games.keys())
    )

    st.balloons()

    st.success(
        f"🎉 Today's Game: {winner}"
    )

    st.session_state["selected_game"] = winner