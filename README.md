# Spotify Song Popularity Prediction

This project uses Spotify audio features to predict whether a song is likely to be popular or not popular.

## Problem Statement

The goal of this project is to understand whether a song's audio features can help predict its popularity. In this project, songs with a popularity score of **70 or higher** are labeled as **popular**, while songs below 70 are labeled as **not popular**.

The main question is:

**Can we use Spotify song features such as danceability, energy, loudness, tempo, and acousticness to predict if a song will be popular?**

## Dataset

The dataset contains Spotify song information, including popularity scores and audio features such as:

- Danceability
- Energy
- Loudness
- Speechiness
- Acousticness
- Instrumentalness
- Liveness
- Valence
- Tempo
- Explicit content

## Methods Used

The project follows a beginner-friendly machine learning process:

- Data loading
- Data cleaning
- Exploratory data analysis
- Feature engineering
- Model building
- Model evaluation
- Probability-based prediction
- Hit song simulation

## Models Used

- Logistic Regression
- Balanced Logistic Regression
- Random Forest Classifier
- A lightweight Random Forest model was trained separately for Streamlit deployment to reduce file size while keeping the same feature inputs and prediction logic.

## What We Were Able To Discover

- Most songs in the dataset are **not popular**, which means the dataset is imbalanced.
- Only a smaller number of songs have a popularity score of 70 or higher.
- Audio features can give useful signals, but they cannot perfectly explain popularity.
- Random Forest was useful because it predicted song popularity and also showed which features were more important.
- Probability scores gave more detail than a simple popular/not popular prediction.
- Some generated song combinations had higher predicted popularity probabilities than others.
- Song popularity is not only based on audio features. Artist fame, playlists, marketing, release timing, and social media trends can also affect popularity.

## Key Insights

- Songs with stronger energy, danceability, and loudness may have a better chance of being predicted as popular.
- Songs with very high acousticness or instrumentalness may be less likely to be predicted as popular in this dataset.
- Since the dataset is imbalanced, balanced models can help the model pay more attention to popular songs.
- It is better to look at prediction probability instead of only checking the final yes/no prediction.

## Conclusion

This project shows how machine learning can be used to estimate Spotify song popularity from audio features. The model can provide helpful predictions and insights, but it should be used as a guide rather than a perfect answer because real-world music popularity depends on many factors outside the dataset.
