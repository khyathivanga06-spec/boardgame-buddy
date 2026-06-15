import streamlit as st
import time
from utils import load_css, sidebar_brand, hero_banner
st.set_page_config(
    page_title="Game Timer",
    page_icon="⏱️",
    layout="wide"
)

load_css()
sidebar_brand()
hero_banner(
    "⏱️ Game Timer",
    "Track Time • Stay Fair • Play Better"
)

time_option = st.selectbox(
    "⏱️ Choose Timer",
    [
        "30 Seconds",
        "1 Minute",
        "2 Minutes",
        "5 Minutes"
    ]
)

if time_option == "30 Seconds":
    seconds = 30

elif time_option == "1 Minute":
    seconds = 60

elif time_option == "2 Minutes":
    seconds = 120

else:
    seconds = 300
st.info(
    f"Selected Time: {seconds} seconds"
)
if st.button("🚀 Start Timer"):

    progress = st.progress(0)

    for i in range(seconds):

        progress.progress(
            (i + 1) / seconds
        )

        time.sleep(1)

    st.balloons()
    st.success(
        "🎉 Time's Up! Challenge Complete!"
    )