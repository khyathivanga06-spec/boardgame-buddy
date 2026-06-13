import streamlit as st
from games_data import games

st.set_page_config(
    page_title="BoardGame Buddy",
    page_icon="🎲",
    layout="wide"
)

# Hero Section
st.markdown("""
<div style="
background: linear-gradient(135deg,#d4fc79,#96e6a1);
padding:30px;
border-radius:20px;
text-align:center;
margin-bottom:20px;
">
<h1>🎲 BoardGame Buddy</h1>
<h3>Learn Board Games in Minutes!</h3>
<p>Watch tutorials • Learn rules • Take quizzes • Become a Board Game Master</p>
</div>
""", unsafe_allow_html=True)

# Search
search = st.text_input(
    "🔍 Search for a Board Game",
    placeholder="Chess, Tangram, Jodo..."
)

st.markdown("---")

st.header("🌟 Featured Games")

# Filter Games
filtered_games = []

for game_name in games.keys():
    if search.lower() in game_name.lower():
        filtered_games.append(game_name)

# Display cards
cols = st.columns(4)

for i, game_name in enumerate(filtered_games):
    game = games[game_name]

    with cols[i % 4]:
        st.image(game["image"])
        st.markdown(f"### {game_name}")
        st.write(f"👥 {game['players']} Players")
        st.write(f"🎂 {game['age']}")
        st.write("⭐" * game["difficulty"])