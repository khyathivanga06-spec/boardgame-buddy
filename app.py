import streamlit as st
from games_data import games

import streamlit as st
from games_data import games

st.set_page_config(
    page_title="BoardGame Buddy",
    page_icon="🎲",
    layout="wide"
)

st.markdown("""
<style>
...
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

.stApp {
    background-color: #32CD32;
}

/* Headers */
h1, h2, h3 {
    color: white !important;
}

/* Text */
p, label {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)
# -----------------------------
# SEARCH BAR
# -----------------------------

search = st.text_input(
    "🔍 Search Games",
    placeholder="Chess, Tangram, Jodo..."
)

# -----------------------------
# CATEGORIES
# -----------------------------

st.subheader("🎮 Categories")

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.button("👨‍👩‍👧 Family")

with c2:
    st.button("🧠 Strategy")

with c3:
    st.button("🎉 Party")

with c4:
    st.button("🧒 Kids")

with c5:
    st.button("🃏 Card")

st.divider()

# -----------------------------
# FEATURED GAMES
# -----------------------------

st.header("⭐ Featured Games")

filtered_games = []

for game_name in games.keys():
    if search.lower() in game_name.lower():
        filtered_games.append(game_name)

for i in range(0, len(filtered_games), 4):

    row_games = filtered_games[i:i+4]

    cols = st.columns(4)

    for col, game_name in zip(cols, row_games):

        game = games[game_name]

        with col:

            st.image(game["image"])

            st.markdown(f"### {game_name}")

            st.write(f"👥 {game['players']} Players")

            st.write(f"🎂 Age: {game['age']}")

            st.write("⭐" * game["difficulty"])

            st.button(
                f"Learn {game_name}",
                key=f"btn_{game_name}"
            )