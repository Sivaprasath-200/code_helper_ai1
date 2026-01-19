import streamlit as st

st.set_page_config(
    page_title="Code Helper AI",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0B132B, #1C2541, #3A506B);
        color: #EAEAEA;
    }

    .hero-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 700;
        color: #D6ECFF;
    }

    .hero-sub {
        text-align: center;
        font-size: 1.1rem;
        color: #A9C6E8;
        margin-bottom: 2rem;
    }

    .card {
        background: rgba(255,255,255,0.06);
        border-radius: 16px;
        padding: 1.5rem;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
    }

    textarea {
        background-color: #0F172A !important;
        color: white !important;
        border-radius: 12px !important;
    }

    .stButton > button {
        background-color: #4FD1C5;
        color: black;
        border-radius: 12px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class="hero-title">Code Helper AI Agent</div>
    <div class="hero-sub">
    AI-powered assistant that analyzes code first<br>
    and gives clean, exam-friendly corrections.
    </div>
    """,
    unsafe_allow_html=True
)
import streamlit as st
from ai_agent import analyze_code

# ---------- CODE INPUT CARD ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("### 📋 Paste your code here")

code = st.text_area(
    label="",
    placeholder="Paste your Python / C / Java / JS code here...",
    height=220
)

analyze = st.button("🔍 Analyze Code")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- RESULT ----------
if analyze:
    if code.strip() == "":
        st.warning("⚠️ Please paste some code first.")
    else:
        with st.spinner("Analyzing code..."):
            result = analyze_code(code)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### ✅ Result")
        st.write(result)
        st.markdown('</div>', unsafe_allow_html=True)
