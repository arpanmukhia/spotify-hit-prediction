import streamlit as st
import pandas as pd
import joblib

model = joblib.load("spotify_hit_app_model.joblib")

st.title("🎧 Spotify Hit Song Predictor")
st.write("Adjust the song features below to estimate the chance of becoming popular.")

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