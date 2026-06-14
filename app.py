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

    background: linear-gradient(
        180deg,
        #111827,
        #1F2937
    );

    border-right: 1px solid rgba(
        255,255,255,0.1
    );
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

    border-radius: 18px;

    padding: 12px;

    font-weight: bold;

    width: 100%;

    transition: all 0.3s ease;

    box-shadow: 0px 5px 15px rgba(
        0,0,0,0.3
    );
}

.stButton > button:hover {

    transform: translateY(-5px);

    box-shadow:
    0px 10px 25px rgba(
        6,182,212,0.5
    );

    cursor: pointer;
}

/* Search box */
.stTextInput input {
    background-color: #1F2937;
    color: white !important;
    border-radius: 12px;
}

/* Cards */
.card {
    background: rgba(
        255,255,255,0.05
    );

    backdrop-filter: blur(10px);

    padding: 20px;

    border-radius: 25px;

    border: 1px solid rgba(
        255,255,255,0.1
    );

    box-shadow:
    0px 8px 25px rgba(
        0,0,0,0.3
    );

    margin-bottom: 20px;

    text-align: center;

    transition: all 0.3s ease;
}

.card:hover {

    transform: translateY(-8px);

    box-shadow:
    0px 15px 35px rgba(
        139,92,246,0.4
    );
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
img {

    transition: all 0.3s ease;

    border-radius: 20px;
}

img:hover {

    transform: scale(1.04);

    box-shadow:
    0px 10px 30px rgba(
        139,92,246,0.5
    );
}
            hr {
    border: none;
    height: 2px;

    background: linear-gradient(
        90deg,
        transparent,
        #8B5CF6,
        #06B6D4,
        transparent
    );

    margin-top: 20px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO BANNER
# -----------------------------

st.markdown("""
<div style="
background:linear-gradient(
135deg,
#7C3AED,
#06B6D4,
#14B8A6
);
padding:40px;
border-radius:25px;
text-align:center;
margin-bottom:25px;
box-shadow:0px 0px 40px rgba(6,182,212,0.4);
">

<h1 style="
color:white;
font-size:60px;
font-weight:800;
margin-bottom:10px;
">
🎲 BoardGame Buddy
</h1>

<h2 style="
color:white;
font-size:34px;
margin-bottom:15px;
">
Become a Board Game Master
</h2>

<p style="
color:white;
font-size:18px;
">
🎯 Complete Challenges • 🧠 Take Quizzes • 🏆 Earn XP • 🎮 Learn Games
</p>

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

st.markdown("""
# ⭐ Featured Games

Explore • Learn • Master
""")

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

            st.markdown(
                '<div class="card">',
                unsafe_allow_html=True
            )

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
st.markdown(
    '</div>',
    unsafe_allow_html=True
)
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