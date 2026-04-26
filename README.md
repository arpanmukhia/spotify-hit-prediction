# Spotify Song Popularity Prediction

This project predicts whether a Spotify song is popular using audio features such as danceability, energy, loudness, acousticness, instrumentalness, valence, tempo, and explicit content.

Songs with a popularity score of **70 or higher** are labeled as popular.

## Workflow

1. Problem statement
2. Data loading
3. Data cleaning
4. Exploratory data analysis
5. Feature engineering
6. Model building
7. Model evaluation
8. Handling class imbalance
9. Probability-based predictions
10. Hit song simulation
11. Key insights
12. Conclusion

## Models Used

- Logistic Regression
- Balanced Logistic Regression
- Random Forest Classifier

## Key Insights

- Most songs in the dataset are not popular, so the dataset is imbalanced.
- Probability scores are more informative than only checking the final prediction.
- Random Forest is useful because it predicts popularity and shows feature importance.
- Real-world popularity also depends on artist fame, playlists, marketing, social media trends, and release timing.

## How To Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Open and run:

```text
spotify-popularity-github.ipynb
```
