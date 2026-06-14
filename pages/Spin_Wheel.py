import streamlit as st
import random
import time
from games_data import games

st.set_page_config(
    page_title="🎲 Random Game",
    page_icon="🎡",
    layout="wide"
)

st.title("🎡 Random Game Selector")

st.write(
    "Get a surprise board game challenge and start learning!"
)

games_list = list(games.keys())

wheel_placeholder = st.empty()

if st.button("🎲 SPIN THE WHEEL"):

    # spinning animation

    for i in range(25):

        current = random.choice(games_list)

        wheel_placeholder.markdown(
            f"""
            <div style="
            text-align:center;
            padding:30px;
            border-radius:20px;
            background:linear-gradient(135deg,#8B5CF6,#06B6D4);
            color:white;
            font-size:35px;
            font-weight:bold;
            ">
            🎡 {current}
            </div>
            """,
            unsafe_allow_html=True
        )

        time.sleep(0.1)

    winner = random.choice(games_list)

    wheel_placeholder.markdown(
        f"""
        <div style="
        text-align:center;
        padding:30px;
        border-radius:20px;
        background:linear-gradient(135deg,#FACC15,#FB7185);
        color:black;
        font-size:40px;
        font-weight:bold;
        ">
        🏆 WINNER<br><br>
        {winner}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.balloons()

    st.session_state["selected_game"] = winner

    st.success(
        f"🎉 Today's challenge: Learn {winner}!"
    )