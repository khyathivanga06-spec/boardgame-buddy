import streamlit as st
from utils import load_css, sidebar_brand, hero_banner
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)
load_css()
sidebar_brand()
hero_banner(
    "📊 Dashboard",
    "Track Progress • XP • Achievements"
)

# Sample progress data

games_completed = 3
total_games = 8

progress = games_completed / total_games

# Top metrics

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎮 Games Learned", games_completed)

with col2:
    st.metric("🏆 Badges Earned", 3)

with col3:
    st.metric("📚 Total Games", total_games)

st.markdown("---")

st.subheader("🚀 Learning Progress")

st.progress(progress)

st.write(f"You have completed **{games_completed} out of {total_games} games!**")

st.markdown("---")

st.subheader("🏆 Badges")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("♟️ Chess Master")

with col2:
    st.success("🃏 Uno Champion")

with col3:
    st.success("🏠 Monopoly Expert")

st.markdown("---")

st.subheader("🎯 Next Goals")

st.info("📖 Learn Tangram")
st.info("🏗️ Learn Jodo")
st.info("🚂 Learn Ticket To Ride")

st.balloons()
