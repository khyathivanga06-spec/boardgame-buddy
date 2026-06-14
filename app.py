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
.stApp {
    background: #0B1020;
}

/* Text */
h1, h2, h3, p, div, label {
    color: #FFF8DC !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(
        135deg,
        #8B5CF6,
        #06B6D4
    );
    color: white !important;
    border: none;
    border-radius: 15px;
    padding: 12px;
    font-weight: bold;
    width: 100%;
}

/* Search box */
.stTextInput input {
    background-color: #1F2937;
    color: white !important;
    border-radius: 12px;
}

/* Cards */
.card {
    background: #151C2E;
    padding: 15px;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    margin-bottom: 20px;
    text-align: center;
}

.challenge-card {
    background: linear-gradient(
        135deg,
        #FACC15,
        #FB7185
    );
    padding: 20px;
    border-radius: 20px;
    color: black !important;
    margin-bottom: 25px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO
# -----------------------------

st.markdown("""
<div style="
background:linear-gradient(135deg,#8B5CF6,#06B6D4);
padding:40px;
border-radius:25px;
text-align:center;
margin-bottom:25px;
">

<h1 style="color:white;">
🎲 BoardGame Buddy
</h1>

<h2 style="color:white;">
Become a Board Game Master
</h2>

<p style="color:white;font-size:18px;">
🎯 Complete Challenges • 🧠 Take Quizzes • 🏆 Earn XP • 🎮 Learn Games
</p>

</div>
""", unsafe_allow_html=True)

# -----------------------------
# XP BAR
# -----------------------------

if "xp" not in st.session_state:
    st.session_state["xp"] = 250

xp = st.session_state["xp"]

level = xp // 100 + 1

st.subheader(
    f"⭐ Level {level} Board Gamer"
)

st.progress(
    min(xp / 1000, 1.0)
)

st.write(
    f"XP: {xp} / 1000"
)

# -----------------------------
# DAILY CHALLENGE
# -----------------------------

st.markdown("""
<div class="challenge-card">

<h3>🎯 DAILY CHALLENGE</h3>

<b>Learn Tangram</b><br>

Score 80% or higher in the quiz.<br><br>

🏆 Reward: +100 XP

</div>
""", unsafe_allow_html=True)

# -----------------------------
# SEARCH
# -----------------------------

search = st.text_input(
    "🔍 Search Games",
    placeholder="Chess, Tangram, Jodo..."
)

st.divider()

# -----------------------------
# CATEGORIES
# -----------------------------

st.header("🎮 Categories")

c1,c2,c3,c4,c5 = st.columns(5)

with c1:
    st.button("👨‍👩‍👧 Family")

with c2:
    st.button("🧠 Strategy")

with c3:
    st.button("🎉 Party")

with c4:
    st.button("🧩 Puzzle")

with c5:
    st.button("🃏 Card")

st.divider()

# -----------------------------
# FEATURED GAMES
# -----------------------------

st.header("⭐ Featured Games")

filtered_games = [
    game for game in games.keys()
    if search.lower() in game.lower()
]

for i in range(0, len(filtered_games), 4):

    row_games = filtered_games[i:i+4]

    cols = st.columns(4)

    for col, game_name in zip(cols, row_games):

        game = games[game_name]

        with col:

            st.image(game["image"])

            st.markdown(
                f"### {game_name}"
            )

            st.write(
                f"👥 {game['players']} Players"
            )

            st.write(
                f"🎂 Age: {game['age']}"
            )

            st.write(
                "⭐" * game["difficulty"]
            )

            if st.button(
                f"🎮 Learn {game_name}",
                key=f"btn_{game_name}"
            ):
                st.session_state["selected_game"] = game_name
                st.switch_page("pages/1_Learn_Games.py")

# -----------------------------
# SPIN WHEEL
# -----------------------------

st.divider()

st.header("🎡 Surprise Me")

if st.button("🎲 Pick a Random Game"):

    import random

    random_game = random.choice(
        list(games.keys())
    )

    st.success(
        f"Today's random game is: {random_game}"
    )