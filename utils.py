import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .stApp {
        background: #0B1020;
    }

    section[data-testid="stSidebar"] {

        background: linear-gradient(
            180deg,
            #111827,
            #1E293B,
            #0F172A
        );
    }

    .stButton > button {

        background: linear-gradient(
            135deg,
            #8B5CF6,
            #06B6D4
        );

        border-radius: 18px;

        transition: all 0.3s ease;
    }

    .stButton > button:hover {

        transform: translateY(-5px);
    }

    img {

        transition: all 0.3s ease;
    }

    img:hover {

        transform: scale(1.03);
    }

    </style>
    """, unsafe_allow_html=True)