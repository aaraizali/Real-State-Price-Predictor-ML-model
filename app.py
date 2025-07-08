import streamlit as st
from streamlit_lottie import st_lottie
import numpy as np
from joblib import load

st.set_page_config(page_title="Real Estate Predictor", layout="wide")

model = load("Real_state.joblib")

lottie_url = "https://assets2.lottiefiles.com/packages/lf20_puciaact.json"

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0f1c2e;
        background-size: cover;
        background-position: center;
        font-family: 'Segoe UI', sans-serif;
    }
    .glass {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2rem;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 30px rgba(0,0,0,0.2);
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white;
    }
    .heading {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
        text-shadow: 2px 2px 8px #000;
        margin-bottom: 0.5rem;
    }
    .subheading {
        text-align: center;
        font-size: 1.2rem;
        color: #f0f0f0;
        margin-bottom: 2rem;
    }
    .predict-btn button {
        background: linear-gradient(to right, #06beb6, #48b1bf);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
        font-size: 1.1rem;
        transition: all 0.3s ease-in-out;
    }
    .predict-btn button:hover {
        box-shadow: 0 0 15px rgba(0,255,255,0.6);
        transform: scale(1.05);
    }
    .result-box {
        background: linear-gradient(to right, #4facfe, #00f2fe);
        padding: 1rem 2rem;
        border-radius: 12px;
        color: white;
        font-size: 1.4rem;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        font-size: 0.9rem;
        color: #cccccc;
    }
    .stNumberInput label, .stSelectbox label {
        font-weight: bold;
        font-size: 1.05rem;
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st_lottie(lottie_url, height=200, speed=1)
st.markdown('<div class="heading">🏡 Real Estate Price Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subheading">Enter the details below to estimate house price in Boston</div>', unsafe_allow_html=True)

with st.container():
    with st.form("predict_form"):
        st.markdown('<div class="glass">', unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            CRIM = st.number_input("Crime Rate per capita (CRIM)", min_value=0.0, value=0.2)
            ZN = st.number_input("Residential Zoned Land % (ZN)", min_value=0.0, value=12.5)
            INDUS = st.number_input("Non-retail Business Acres % (INDUS)", min_value=0.0, value=23.0)
            chas_option = st.selectbox("Charles River Tract? (CHAS)", ["No", "Yes"])
            CHAS = 1 if chas_option == "Yes" else 0


        with col2:
            NOX = st.number_input("Nitric Oxides Concentration (NOX)", min_value=0.0, value=0.5)
            RM = st.number_input("Average Rooms per Dwelling (RM)", min_value=0.0, value=6.0)
            AGE = st.number_input("% Units Built Before 1940 (AGE)", min_value=0.0, value=68.0)
            DIS = st.number_input("Distance to Employment Centers (DIS)", min_value=0.0, value=4.5)

        with col3:
            RAD = st.number_input("Highway Accessibility Index (RAD)", min_value=0.0, value=1.0)
            TAX = st.number_input("Property Tax Rate (TAX)", min_value=0.0, value=296.0)
            PTRATIO = st.number_input("Pupil-Teacher Ratio (PTRATIO)", min_value=0.0, value=18.0)
            B = st.number_input("Proportion of Black Population (B)", min_value=0.0, value=390.0)

        col_spacer1, col_center, col_spacer2 = st.columns([1, 2, 1])
        with col_center:
            LSTAT = st.number_input("Lower Status Population % (LSTAT)", min_value=0.0, value=12.0)

        st.markdown('</div>', unsafe_allow_html=True)
        submitted = st.form_submit_button("Predict", type="primary")

    if submitted:
        input_data = np.array([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE,
                                DIS, RAD, TAX, PTRATIO, B, LSTAT]])
        prediction = model.predict(input_data)
        st.markdown(f'<div class="result-box">💰 Estimated Price: ${round(prediction[0]*1000, 2)}</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">🔧 Built with ❤️ by <b>Aaraiz Ali</b> | Powered by Streamlit</div>', unsafe_allow_html=True)
