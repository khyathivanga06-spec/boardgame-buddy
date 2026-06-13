import streamlit as st
from games_data import games

st.set_page_config(
    page_title="BoardGame Buddy",
    page_icon="🎲",
    layout="wide"
)

# Header
st.title("🎲 BoardGame Buddy")
st.subheader("Learn Board Games in Minutes")

st.markdown("---")

# Select Game
selected_game = st.selectbox(
    "Choose a Board Game",
    list(games.keys())
)

game = games[selected_game]

st.markdown("---")

# Game Information
st.header(selected_game)

col1, col2 = st.columns(2)

with col1:
    st.write(f"👥 Players: {game['players']}")
    st.write(f"🎂 Recommended Age: {game['age']}")
    st.write(f"⏱️ Play Time: {game['time']}")

with col2:
    st.write("Difficulty")
    st.write("⭐" * game["difficulty"])

st.markdown("---")

# Video Tutorial
st.subheader("🎥 Watch and Learn")
st.video(game["video"])

st.markdown("---")

# Rules
st.subheader("📚 Simplified Rules")

col1, col2 = st.columns(2)

with col1:
    st.info(f"### Setup\n\n{game['setup']}")

with col2:
    st.info(f"### How To Play\n\n{game['play']}")

col3, col4 = st.columns(2)

with col3:
    st.warning(f"### Special Rules\n\n{game['special']}")

with col4:
    st.success(f"### How To Win\n\n{game['win']}")