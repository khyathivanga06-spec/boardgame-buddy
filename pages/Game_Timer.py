import streamlit as st
import time

st.title("⏱️ Game Timer")

seconds = st.slider(
    "Choose Time",
    10,
    300,
    60
)

if st.button("Start Timer"):

    progress = st.progress(0)

    for i in range(seconds):

        progress.progress(
            (i + 1) / seconds
        )

        time.sleep(1)

    st.balloons()

    st.success(
        "⏰ Time's Up!"
    )