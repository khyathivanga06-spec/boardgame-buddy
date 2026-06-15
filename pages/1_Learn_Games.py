import streamlit as st
from games_data import games
from quiz import quiz_data
from utils import load_css, sidebar_brand, hero_banner

st.set_page_config(
    page_title="Learn Games",
    page_icon="🎲",
    layout="wide"
)
load_css()
sidebar_brand()
# Styling

st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
}

h1,h2,h3 {
    color: #FFF8DC !important;
}

label {
    color: #FFF8DC !important;
}

.stSelectbox div[data-baseweb="select"] {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# Hero

hero_banner(
    "🎮 Learn Games",
    "Explore Rules • Learn Strategies • Become a Master"
)

# Auto-open selected game

default_game = st.session_state.get(
    "selected_game",
    list(games.keys())[0]
)

selected_game = st.selectbox(
    "Choose a Board Game",
    list(games.keys()),
    index=list(games.keys()).index(default_game)
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
    st.write(f"⏱️ Play Time: {game['time']}")

with col2:
    st.write("Difficulty")
    st.write("⭐" * game["difficulty"])

st.divider()

st.subheader("🎥 Watch and Learn")

st.video(game["video"])

st.divider()

st.subheader("📚 Simplified Rules")

c1, c2 = st.columns(2)

with c1:
    st.info(f"### Setup\n\n{game['setup']}")

with c2:
    st.info(f"### How To Play\n\n{game['play']}")

c3, c4 = st.columns(2)

with c3:
    st.warning(f"### Special Rules\n\n{game['special']}")

with c4:
    st.success(f"### How To Win\n\n{game['win']}")

    st.divider()

st.subheader("🧠 Quiz Time")

if selected_game in quiz_data:

    score = 0

    answers = []

    for i, q in enumerate(quiz_data[selected_game]):

        answer = st.radio(
            q["question"],
            q["options"],
            key=f"{selected_game}_{i}"
        )

        answers.append(answer)

    if st.button("Submit Quiz"):

        for answer, q in zip(
            answers,
            quiz_data[selected_game]
        ):
            if answer == q["answer"]:
                score += 1

        st.success(
            f"You scored {score}/{len(quiz_data[selected_game])}"
        )

        percentage = (
            score /
            len(quiz_data[selected_game])
        ) * 100

        st.progress(int(percentage) / 100)

        if percentage >= 80:
            if "xp" not in st.session_state:
                st.session_state["xp"] = 0

            st.session_state["xp"] += 100

            st.balloons()

            st.success(
                "🏆 Badge Unlocked! +100 XP"
            )

# -----------------------------
# TANGRAM CHALLENGE
# -----------------------------

if selected_game == "Tangram":

    st.divider()

    st.header("🧩 Tangram Cat Challenge")

    st.write(
        "Move the slider to see each building step!"
    )

    if "tangram_step" not in st.session_state:
        st.session_state["tangram_step"] = 1

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "⬅ Previous",
            key="tangram_prev"
        ):

            if st.session_state["tangram_step"] > 1:

                st.session_state["tangram_step"] -= 1

    with col2:

        if st.button(
            "Next ➡",
            key="tangram_next"
        ):

            if st.session_state["tangram_step"] < 4:

                st.session_state["tangram_step"] += 1

    step = st.session_state["tangram_step"]

    st.image(
        f"assets/tangram_steps/step{step}.jpg",
        caption=f"Step {step}"
    )

    if step == 4:

        st.balloons()

        st.success(
            "🎉 Challenge Complete! You built the Tangram Cat!"
        )

    uploaded_file = st.file_uploader(
        "📸 Upload your Tangram Creation",
        type=["jpg", "jpeg", "png"],
        key="tangram_upload"
    )

    if uploaded_file:

        st.image(
            uploaded_file,
            caption="Your Tangram Creation"
        )

        st.success(
            "🏆 Awesome work! Tangram Challenge Submitted!"
        )

# -----------------------------
# JODO CHALLENGE
# -----------------------------

if selected_game == "Jodo":

    st.divider()

    st.header("🏗️ Jodo House Challenge")

    st.write(
        "Follow the building steps!"
    )

    if "jodo_step" not in st.session_state:
        st.session_state["jodo_step"] = 1

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "⬅ Previous",
            key="jodo_prev"
        ):

            if st.session_state["jodo_step"] > 1:

                st.session_state["jodo_step"] -= 1

    with col2:

        if st.button(
            "Next ➡",
            key="jodo_next"
        ):

            if st.session_state["jodo_step"] < 4:

                st.session_state["jodo_step"] += 1

    step = st.session_state["jodo_step"]
    st.progress(step / 4)

    st.write(
        f"🏗️ Step {step} of 4"
    )
    st.image(
        f"assets/jodo_steps/step{step}.jpg",
        caption=f"Step {step}"
    )

    if step == 4:

        st.balloons()

        st.success(
            "🎉 Awesome! You built a Jodo House!"
        )

    uploaded_file = st.file_uploader(
        "📸 Upload your Jodo Creation",
        type=["jpg", "jpeg", "png"],
        key="jodo_upload"
    )

    if uploaded_file:

        st.image(
            uploaded_file,
            caption="Your Jodo Creation"
        )

        st.success(
            "🏆 Amazing build! Challenge Submitted!"
        )