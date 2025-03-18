# Twitter Sentiment Analysis 

## Overview
This project is a **Sentiment Analysis App** that classifies user-input text as either **positive, negative, or neutral** using a pre-trained machine learning model. 

The app is built using **Streamlit**, providing a simple web interface for real-time sentiment analysis.

## Features
- **Machine Learning Model**: Uses a pre-trained sentiment analysis model.
- **User-Friendly Interface**: Built with **Streamlit** for ease of use.
- **Real-Time Sentiment Analysis**: Users can enter text and instantly receive sentiment classification.

## Files
- **`app1.py`** - Streamlit app that loads the trained sentiment model, collects user input, and predicts sentiment.
- **`sentiment_model.pkl`** - Pre-trained machine learning model for sentiment classification.
- **`Twitter(1).ipynb`** - Jupyter Notebook containing the model training and preprocessing workflow.


## Model & Data Processing
- The model was trained using a dataset of text labeled with sentiment.
- Preprocessing steps (e.g., tokenization, stopword removal) are applied to input text before prediction.
- The model classifies input text as **positive, negative, or neutral**.

