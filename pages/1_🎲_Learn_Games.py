import streamlit as st
from games_data import games

st.title("🎲 Learn Games")

selected_game = st.selectbox(
    "Choose a Board Game",
    list(games.keys())
)

game = games[selected_game]

st.header(selected_game)

st.image(
    game["image"],
    width=500
)

col1, col2 = st.columns(2)

with col1:
    st.write(f"👥 Players: {game['players']}")
    st.write(f"🎂 Age: {game['age']}")
    st.write(f"⏱️ Time: {game['time']}")

with col2:
    st.write("Difficulty")
    st.write("⭐" * game["difficulty"])

st.markdown("---")

st.subheader("🎥 Watch and Learn")

st.video(game["video"])

st.markdown("---")

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
