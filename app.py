import streamlit as st
from games_data import games

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="BoardGame Buddy",
    page_icon="🎲",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

/* Background */
..stApp {
    background-color: #C8F5C8;
}

/* Headers */
h1, h2, h3 {
    color: #1E3A5F !important;
}

/* General text */
p, label {
    color: #334155 !important;
}

/* Buttons */
.stButton > button {
    background-color: #111827;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 10px;
}

/* Search box */
.stTextInput input {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO BANNER
# -----------------------------

st.markdown("""
<div style="
background: linear-gradient(135deg,#FFF8DC,#B2F7EF);
padding:35px;
border-radius:25px;
text-align:center;
margin-bottom:20px;
box-shadow:0px 4px 12px rgba(0,0,0,0.2);
">

<h1 style="color:#1E3A5F;">
🎲 BoardGame Buddy
</h1>

<h2 style="color:#1E3A5F;">
Learn Board Games in Minutes
</h2>

<p style="color:#334155; font-size:18px;">
Watch Tutorials • Learn Rules • Take Quizzes • Earn Badges
</p>

</div>
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