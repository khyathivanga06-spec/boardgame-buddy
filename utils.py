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

    section[data-testid="stSidebar"] [aria-current="page"] {

        background: linear-gradient(
            135deg,
            #8B5CF6,
            #06B6D4
        ) !important;

        border-radius: 18px;
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
div[data-testid="stVerticalBlock"] {
    transition: all 0.3s ease;
}

div[data-testid="stVerticalBlock"]:hover {
    transform: translateY(-5px);
}
    </style>
    """, unsafe_allow_html=True)


def hero_banner(title, subtitle):

    st.markdown(f"""
    <div style="
    background:linear-gradient(
    135deg,
    #7C3AED,
    #06B6D4,
    #14B8A6
    );
    padding:35px;
    border-radius:25px;
    text-align:center;
    margin-bottom:25px;
    box-shadow:0px 0px 30px rgba(6,182,212,0.3);
    ">

    <h1 style="color:white;">
    {title}
    </h1>

    <p style="color:white;font-size:18px;">
    {subtitle}
    </p>

    </div>
    """, unsafe_allow_html=True)


def sidebar_brand():

    st.sidebar.markdown("---")

    st.sidebar.markdown("""
    # 🎲 BoardGame Buddy

    Learn • Play • Master
    """)