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
    background-color: #0E1117;
}

/* Headers */
h1, h2, h3 {
    color: #FFF8DC !important;
}

/* Text */
p, label, div {
    color: #FFF8DC;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(
        135deg,
        #8B5CF6,
        #06B6D4
    );
    color: white !important;
    border-radius: 15px;
    border: none;
    padding: 10px;
    font-weight: bold;
}

/* Search Box */
.stTextInput input {
    background-color: #1F2937;
    color: white !important;
    border-radius: 12px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
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
# SEARCH
# -----------------------------

search = st.text_input(
    "🔍 Search Games",
    placeholder="Chess, Tangram, Jodo..."
)

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

            if st.button(
                f"🎮 Learn {game_name}",
                key=f"btn_{game_name}"
            ):
                st.session_state["selected_game"] = game_name

                try:
                    st.switch_page("pages/Learn_Games.py")
                except:
                    st.success(
                        f"{game_name} selected! Open Learn Games from the sidebar."
                    )