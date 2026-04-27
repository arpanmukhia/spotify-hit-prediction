import streamlit as st
import pandas as pd
import joblib
st.set_page_config(
    page_title="Spotify Hit Song Predictor",
    page_icon="🎧",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-color: #000000;
    color: white;
}

h1, h2, h3, p, label {
    color: white !important;
}

.stButton > button {
    background-color: #1DB954;
    color: black;
    border-radius: 10px;
    padding: 10px 24px;
    font-weight: bold;
    border: none;
}

.stButton > button:hover {
    background-color: #1ed760;
    color: black;
}

.stSlider label {
    color: white !important;
}

[data-testid="stMetricValue"] {
    color: #1DB954;
}

.spotify-card {
    background-color: #111111;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #1DB954;
    box-shadow: 0px 0px 20px rgba(29, 185, 84, 0.25);
    text-align: center;
}

.footer {
    text-align: center;
    color: #b3b3b3;
    margin-top: 40px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* Slider track */
div[data-baseweb="slider"] > div {
    background-color: white !important;
}

/* Slider filled part (left side) */
div[data-baseweb="slider"] div div {
    background-color: #1DB954 !important;
}

/* Slider handle (circle) */
div[data-baseweb="slider"] [role="slider"] {
    background-color: white !important;
    border: 2px solid #1DB954 !important;
}

</style>
""", unsafe_allow_html=True)

model = joblib.load("spotify_hit_app_model.joblib")

st.markdown("""
<div class="spotify-card">
    <h1>🎧 Spotify Hit Song Predictor</h1>
    <p>Adjust the song features and predict hit potential using machine learning.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
danceability = st.slider("Danceability", 0.0, 1.0, 0.70)
energy = st.slider("Energy", 0.0, 1.0, 0.75)
loudness = st.slider("Loudness", -30.0, 0.0, -5.0)
speechiness = st.slider("Speechiness", 0.0, 1.0, 0.05)
acousticness = st.slider("Acousticness", 0.0, 1.0, 0.20)
instrumentalness = st.slider("Instrumentalness", 0.0, 1.0, 0.00)
liveness = st.slider("Liveness", 0.0, 1.0, 0.10)
valence = st.slider("Valence", 0.0, 1.0, 0.50)
tempo = st.slider("Tempo", 50.0, 220.0, 120.0)
explicit = st.selectbox("Explicit", [0, 1])

if st.button("Predict Hit Probability"):
    input_data = pd.DataFrame([{
        "danceability": danceability,
        "energy": energy,
        "loudness": loudness,
        "speechiness": speechiness,
        "acousticness": acousticness,
        "instrumentalness": instrumentalness,
        "liveness": liveness,
        "valence": valence,
        "tempo": tempo,
        "explicit": explicit
    }])

    probability = model.predict_proba(input_data)[0][1]

    st.subheader(f"Hit Probability: {round(probability * 100, 2)}%")

    if probability >= 0.20:
        st.success("This song has hit potential ✅")
    else:
        st.warning("This song is less likely to become popular ❌")

st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#b3b3b3;'>Made by <b style='color:#1DB954;'>Arpan Mukhia</b> | Machine Learning Project</p>",
    unsafe_allow_html=True
)        