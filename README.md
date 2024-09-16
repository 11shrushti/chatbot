# Sentiment Analysis with VADER using NLTK

This repository contains a simple implementation of sentiment analysis using the VADER (Valence Aware Dictionary and sEntiment Reasoner) model from the NLTK library. VADER is a lexicon and rule-based sentiment analysis tool specifically designed to analyze social media and other short texts, though it works well on other types of text as well.

## Usage

Once everything is set up, you can use the script to perform sentiment analysis on any given text.

1. **Run the code:**

   In `main.py`, the sentiment analysis function `analyze_sentiment(text: str)` takes a string as input and returns a compound sentiment score between -1 (very negative) and 1 (very positive).

   ```python
   from nltk.sentiment.vader import SentimentIntensityAnalyzer

   # Initialize the sentiment analyzer
   analyzer = SentimentIntensityAnalyzer()

   # Function to analyze sentiment
   def analyze_sentiment(text: str):
       sentiment = analyzer.polarity_scores(text)
       return sentiment["compound"]

Functionality
The script uses VADER to perform sentiment analysis on the given text.
It returns a compound score that summarizes the overall sentiment:
Positive sentiment: Compound score > 0
Neutral sentiment: Compound score = 0
Negative sentiment: Compound score < 0


   
